import atexit
import os
import re
import threading
import random
from time import perf_counter
import numpy as np
import cv2
from pytesseract import pytesseract
from core.exceptions import *
from core.fighter import Fighter
from core.log import log
from core.utils import retry
from core import env, dofus
from core.zone import Zone

work_dir = os.path.dirname(os.path.abspath(__file__))


class FightsFarmer(threading.Thread):

    def __init__(self, top_left, bot_right):
        threading.Thread.__init__(self, name='FightFarmer')
        self.killsig = threading.Event()
        self.stopRetry = threading.Event()
        self.lock = threading.Lock()
        self.fighter_thread = Fighter(dofus.SOURNOISERIE, parent=self)
        self.botRightMap = bot_right
        self.topLeftMap = top_left
        self.harvestZone = Zone(top_left, bot_right)
        print(self.harvestZone.to_dict())
        self.currMap = None

    def run(self):
        self.fighter_thread.start()
        try:
            while not self.killsig.is_set():
                currCoords = self.currMapCoords()
                log.info(f"Current map {currCoords}")
                if not self.harvestZone.inside(*currCoords):
                    self.moveToZone()
                self.harvestCurrMap()
                self.randomWalk()
        except Exception as e:
            log.info("Fatal error in main loop!", exc_info=True)
            self.interrupt()
        log.info("Goodbye cruel world!")

    def randomWalk(self):
        while not self.killsig.is_set():
            log.info(f"Current map {self.currMapCoords()}")
            print(self.currMap.neighbors)
            nx, ny = random.choice(list(self.currMap.neighbors))
            try:
                self.moveTo(nx, ny, nbr_retries=3)
                break
            except ChangeMapFailed as e:
                log.info(str(e))
                self.currMap.neighbors.remove((nx, ny))

    @retry
    def moveTo(self, x, y, timeout=20):
        with self.lock:
            log.info(f"Changing map to {(x, y)}")
            currx, curry = self.currMapCoords()
            direction = x - currx, y - curry
            dofus.mapChangeLoc[direction].click()
            dofus.COMBAT_R.hover()
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < timeout:
            with self.lock:
                if self.currMapCoords() != (currx, curry):
                    return
        raise ChangeMapFailed("Change map timed out!", (x, y))

    def harvestCurrMap(self):
        try:
            if self.currMap.farmable:
                self.harvestCombats(nbr_retries=3)
        except TimeoutError:
            self.currMap.farmable = False

    @retry
    def harvestCombats(self):
        while not self.killsig.is_set():
            log.info("Searching for mobs group...")
            tgt = dofus.COMBAT_R.findAny(dofus.mobs, threshold=0.75, shuffle=True)
            if tgt:
                log.info("I found a mob group")
                self.enterCombat(tgt)
                self.fighter_thread.combatEnded.wait()
                if self.fighter_thread.died:
                    log.info("Bot died during combat!")
            else:
                log.info("Didn't find any mobs here")
                # cv2.imwrite(os.path.join(work_dir, "mapCapture.png"), dofus.COMBAT_R.bi)
                return True

    def enterCombat(self, tgt, timeout=5):
        with self.lock:
            tgt.click()
            log.info("Clicked on mobs group")
        if self.fighter_thread.combatDetected.wait(timeout):
            return True
        log.info("Couldn't open combat!")
        raise TimeoutError("Enter combat timed out!")

    def interrupt(self):
        log.info(f"I farmed {self.fighter_thread.nbr_fights} fights")
        self.fighter_thread.interrupt()
        self.killsig.set()
        self.stopRetry.set()
        file_path = os.path.join(work_dir, "graph.json")
        self.harvestZone.saveTo(file_path)

    def currMapCoords(self):
        image = env.capture(dofus.MAP_COORDS_R)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lower_blue = np.array([228, 220, 220])
        upper_blue = np.array([255, 230, 255])
        bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mask = cv2.inRange(bgr_img, lower_blue, upper_blue)
        result = cv2.bitwise_and(gray, gray, mask=mask)
        result = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY_INV)[1]
        text = pytesseract.image_to_string(result, config='--psm 6')
        res = re.findall("(-?\d+),?(-?\d+)", text)
        currCoords = int(res[0][0]), int(res[0][1])
        if res:
            if self.harvestZone.inside(*currCoords):
                self.currMap = self.harvestZone[currCoords]
            return currCoords
        else:
            raise ParseMapCoordsFailed(f"Enable to parse map coords from {text}")

    def moveToZone(self):
        exclude = set()
        while not self.killsig.is_set():
            try:
                path = self.harvestZone.pathToEntry(self.currMapCoords(), exclude)
                for x, y in path:
                    self.moveTo(x, y, timeout=11, nbr_retries=2)
                return True
            except ChangeMapFailed as e:
                exclude.add(e.coords)


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    env.focusDofusWindow()
    top_left = (8, -21)
    bot_right = (12, -15)
    fighter = FightsFarmer(top_left, bot_right)
    atexit.register(tearDown, fighter)
    fighter.start()
    fighter.join()
    env.focusIDEWindow()
