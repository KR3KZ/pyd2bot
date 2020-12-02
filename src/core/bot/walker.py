import collections
import datetime
import logging
import random
import re
from threading import Timer
from time import perf_counter, sleep

import cv2
import numpy as np
import pyautogui
from pytesseract import pytesseract

from core.exceptions import *
from core import dofus, Region, env
from core.bot import Bot


class Walker(Bot):

    def __init__(self, workdir, name="Dofus"):
        super(Walker, self).__init__(workdir, name=name)
        self.currPos = None
        self.lastPos = None
        self.tmpIgnore = []
        self.zone = None
        self.startZaap = None
        self.memoTime = 60 * 15

    def updatePos(self, nbr_tries=5):
        for i in range(nbr_tries):
            self.currPos = self.parseMapCoords()
            if self.currPos:
                return self.currPos
            if self.disconnected.wait(2):
                self.connected.wait()
        raise ParseMapCoordsFailed(f"Enable to parse map coords")

    def changeMap(self, direction, max_tries=3):
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < max_tries:
            currx, curry = self.updatePos()
            dstx, dsty = currx + direction[0], curry + direction[1]
            directionLocs = dofus.mapChangeLoc[direction]
            random.shuffle(directionLocs)
            for tgt in directionLocs:
                with self.lock:
                    pyautogui.keyDown('shift')
                    sleep(0.1)
                    tgt.click()
                    sleep(0.1)
                    pyautogui.keyUp('shift')
                    dofus.OUT_OF_COMBAT_R.hover()
                if self.waitMapChange(dstx, dsty, self.mapChangeTimeOut):
                    self.lastPos = (currx, curry)
                    return True
                else:
                    dofus.OUT_OF_COMBAT_R.click()
                    sleep(0.1)
            nbr_fails += 1
        return False

    def waitMapChange(self, x, y, timeout=20):
        logging.debug(f"Current map coords: {self.currPos}")
        logging.debug(f"Changing map to destination ({x}, {y})")
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < timeout:
            if self.updatePos() == (x, y):
                logging.debug(f"Change map took {perf_counter() - s}")
                return True
        return False

    def moveToTargets(self, targets):
        self.updatePos()
        exclude = []
        while not self.killsig.is_set():
            path = self.pathToTargets(targets, exclude)
            res = True
            for idx, (x, y) in enumerate(path):
                currx, curry = self.currPos
                direction = x - currx, y - curry
                if not self.changeMap(direction, max_tries=2):
                    exclude.append([self.currPos, (x, y)])
                    res = False
                    break
            if res:
                return True
        return False

    def pathToTargets(self, targets, exclude):
        seen = {self.currPos}
        queue = collections.deque([[self.currPos]])
        while queue:
            path = queue.popleft()
            if path not in exclude and path[-1] in targets:
                return path[1:]
            for coords in self.mapNeighbors(path[-1]):
                next_path = path + [coords]
                if coords not in seen and [path[-1], coords] not in exclude:
                    queue.append(next_path)
                    seen.add(coords)
        raise FindPathFailed("Enable to find a valid path!")

    @staticmethod
    def mapNeighbors(pos):
        directions = {dofus.UP, dofus.DOWN, dofus.LEFT, dofus.RIGHT}
        ans = []
        for direction in directions:
            dx, dy = direction
            dst = pos[0] + dx, pos[1] + dy
            ans.append(dst)
        return ans

    def moveToZone(self, zone):
        return self.moveToTargets(zone)

    def moveToMap(self, dst):
        return self.moveToTargets([dst])

    def randomWalk(self, zone):
        while not self.killsig.is_set():
            dst, direction = zone[self.currPos].randDirection(self.lastPos, ignore=self.tmpIgnore)
            if self.changeMap(direction, max_tries=1):
                return True
            else:
                if self.disconnected.is_set():
                    self.connected.wait()
                else:
                    if self.currPos not in self.zone:
                        self.moveToZone(self.zone)
                    zone[self.currPos].excludeMap(self.lastPos, dst)

    def discharge(self):
        pyautogui.press(dofus.RAPPEL_POTION_SHORTCUT)
        sleep(2)
        self.updatePos()
        self.changeMap(dofus.RIGHT)
        sleep(2)
        Region(1067, 440, 25, 43).click()  # enter bank click
        dofus.BANK_MAN_R.waitAppear(dofus.BANK_MAN_P)
        dofus.BANK_MAN_R.click()  # click on bank man
        dofus.BANK_MAN_TALK_R.waitAppear(dofus.BANK_MAN_TALK_P)
        Region(771, 737, 272, 40).click()  # click first choice
        dofus.INV_OPEN_R.waitAppear(dofus.INVENTAIRE_P)
        Region(1469, 142, 29, 26).click()  # choose resources tab
        sleep(2)
        self.transferAllObjects()
        Region(1418, 146, 28, 15).click()  # choose consumable tab
        sleep(2)
        Region(1354, 810, 44, 5).click()  # click on search region
        sleep(2)
        pyautogui.write("sac")
        self.transferAllObjects()
        Region(1526, 109, 52, 22).click()  # close
        sleep(1)

    def transferAllObjects(self):
        Region(1248, 138, 34, 33).click()  # click transfer
        sleep(2)
        Region(1276, 178, 222, 23).click()  # click transfer visible
        dofus.INV_FIRST_SLOT_R.waitAppear(dofus.EMPTY_SLOT_INV_P)

    def onTimer(self):
        if self.tmpIgnore:
            self.tmpIgnore.pop(0)

    def run(self):
        if not self.resourcesToFarm:
            self.resourcesToFarm = self.patterns.keys()
        self.disconnectedObs.start()
        env.focusDofusWindow(self.name)
        s = perf_counter()
        self.updatePos()
        print(self.currPos)
        while not self.killsig.is_set():
            try:
                if self.fullPods():
                    self.discharge()
                if self.currPos not in self.zone:
                    self.goToZaap(self.startZaap)
                    self.moveToZone(self.zone)
                self.updatePos()
                self.tmpIgnore.append(self.currPos)
                Timer(self.memoTime, self.onTimer).start()
                self.harvest()
                if self.combatStarted.is_set():
                    self.combatEnded.wait()
                self.randomWalk(self.zone)
            except Exception as e:
                if self.disconnected.is_set():
                    self.connected.wait()
                else:
                    logging.error("Fatal error!", exc_info=True)
                    self.interrupt()
                    break
        total_time = str(datetime.timedelta(seconds=perf_counter() - s))
        logging.info(f"farmed for total time: {total_time}.")
        logging.info("Goodbye cruel world!")

    def goToZaap(self, zapCoords):
        print("moving to zaap: ", zapCoords)
        pyautogui.press(dofus.HAVRE_SAC_SHORTCUT)
        sleep(2)
        dofus.HAVRE_SAC_ZAAP_R.click()
        sleep(2)
        while dofus.ZAAP_SCROLL_BAR_END_L.getpixel() != dofus.ZAAP_END_SCROLL_C:
            print(dofus.ZAAP_SCROLL_BAR_END_L.getpixel())
            for k in range(9):
                box_h = dofus.ZAAP_COORD_R.height() / 9
                box_y = dofus.ZAAP_COORD_R.y() + k * box_h
                box_x = dofus.ZAAP_COORD_R.x()
                box_w = dofus.ZAAP_COORD_R.width()
                box_r = Region(box_x, box_y, box_w, box_h)
                image = env.capture(box_r)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                low_bound = np.array([145, 0, 0])
                upper_bound = np.array([255, 255, 14])
                bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                mask = cv2.inRange(bgr_img, low_bound, upper_bound)
                result = cv2.bitwise_and(gray, gray, mask=mask)
                result = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY_INV)[1]
                newShape = (int(box_w * 15), int(box_h * 15))
                result = cv2.resize(result, newShape)
                result = cv2.blur(result, (5, 5))
                text = pytesseract.image_to_string(result, config='--psm 6')
                res = re.findall("(-?\s*\d+),?(-?\s*\d+)", text)
                if res:
                    coord = tuple(map(lambda x: int(x.replace(' ', '')), res[0]))
                    print(coord)
                    if coord == zapCoords:
                        box_r.click()
                        sleep(0.2)
                        box_r.click()
                        self.waitMapChange(*zapCoords, 60 * 15)
                        if zapCoords == (20, -29):
                            Region(618, 729, 36, 24).click()
                        return True
            dofus.ZAAP_COORD_R.scroll(clicks=-3, delay_between_ticks=0.1)
            dofus.OUT_OF_COMBAT_R.hover()
            sleep(0.5)
        raise Exception("Zaap coords not found!")
