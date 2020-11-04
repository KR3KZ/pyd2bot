import atexit
import os
import re
import threading
import random
import numpy as np
import cv2
import yaml
from pytesseract import pytesseract
from core.exceptions import ChangeMapFailed
from core.fighter import Fighter
from core.log import Log
from core.utils import retry
from core import env, dofus

log = Log()
curr_dir = os.path.dirname(os.path.abspath(__file__))


class FightsFarmer(threading.Thread):

    def __init__(self, startMap, endMap, path_to_start, curr=None):
        threading.Thread.__init__(self, name='FightFarmer')
        if not curr:
            curr = startMap
        self.killsig = threading.Event()
        self.stopRetry = threading.Event()
        self.lock = threading.Lock()
        self.fighter_thread = Fighter(dofus.SOURNOISERIE, parent=self)
        self.currMap = curr
        self.endMap = endMap
        self.startMap = startMap
        self.memo = {}
        self.exclude = set()
        self.pathToStart = path_to_start

    def inZone(self, mapCoords):
        mapx, mapy = mapCoords
        return self.startMap[0] <= mapx <= self.endMap[0] and \
               self.startMap[1] <= mapy <= self.endMap[1]

    def randNextMap(self):
        moves = {dofus.UP, dofus.DOWN, dofus.LEFT, dofus.RIGHT}
        while not self.killsig.is_set():
            direction = random.choice(list(moves - self.memo[self.currMap]))
            nextMap = self.nextMap(direction)
            if nextMap not in self.exclude and self.inZone(nextMap):
                return direction, nextMap
            else:
                self.memo[self.currMap].add(direction)

    def run(self):
        self.loadMemo()
        self.fighter_thread.start()
        try:
            while not self.killsig.is_set():
                self.moveToStartMap()
                while not self.killsig.is_set():
                    try:
                        log.info(f"Current map {self.currMap}")
                        if self.findCombat(nbr_retries=3):
                            self.fighter_thread.combatEnded.wait()
                            if self.fighter_thread.died:
                                log.info("Bot died during combat!")
                                break
                    except TimeoutError:
                            log.info(f"I will exclude {self.currMap}")
                            self.exclude.add(self.currMap)
                    self.randomWalk()
        except Exception as e:
            log.info(exc_info=True)
            self.interrupt()
        log.info("Goodbye cruel world!")

    def nextMap(self, direction):
        return self.currMap[0] + direction[0], self.currMap[1] + direction[1]

    def moveToStartMap(self):
        log.info(f"Moving from {self.currMap} to start map {self.startMap}")
        for direction in self.pathToStart:
            self.changeMap(direction)

    def loadMemo(self):
        file_path = os.path.join(curr_dir, "memo.yaml")
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                self.exclude = data["exclude"]
                self.memo = data["memo"]

    def randomWalk(self):
        if self.currMap not in self.memo:
            self.memo[self.currMap] = set()
        while not self.killsig.is_set():
            direction = self.randNextMap()
            try:
                self.changeMap(direction)
                break
            except ChangeMapFailed as e:
                log.info(str(e))
                self.memo[self.currMap].add(direction)

    @retry
    def findCombat(self):
        while not self.killsig.is_set():
            log.info("Searching for mobs group...")
            tgt = dofus.COMBAT_R.findAny(dofus.mobs, threshold=0.75, shuffle=True)
            if tgt:
                log.info("I found a mob group")
                self.enterCombat(tgt, nbr_retries=2)
                return True
            else:
                log.info("Didn't find any mobs here")
                cv2.imwrite(os.path.join(curr_dir, "mapCapture.png"), dofus.COMBAT_R.bi)
                return False

    @retry
    def enterCombat(self, tgt, timeout=5):
        with self.lock:
            tgt.click()
            log.info("Clicked on mobs group")
        if self.fighter_thread.combatDetected.wait(timeout):
            return True
        log.info("Couldn't open combat!")
        raise TimeoutError("Enter combat timed out!")

    @retry
    def changeMap(self, direction, timeout=20):
        with self.lock:
            nextMap = self.nextMap(direction)
            log.info(f"Changing map to {nextMap}")
            if direction == dofus.DOWN:
                dofus.MAP_DOWN_L.click()
            elif direction == dofus.UP:
                dofus.MAP_UP_L.click()
            elif direction == dofus.LEFT:
                dofus.MAP_LEFT_L.click()
            elif direction == dofus.RIGHT:
                dofus.MAP_RIGHT_L.click()
            dofus.COMBAT_R.hover()
        if dofus.MINIMAP_R.waitChange(timeout):
            if self.fighter_thread.combatDetected.wait(1):
                raise ChangeMapFailed("Change map failed due to agro!")
            self.currMap = nextMap
            return True
        raise ChangeMapFailed("Change map timed out!")

    def interrupt(self):
        log.info(f"I farmed {self.fighter_thread.nbr_fights} fights")
        self.fighter_thread.interrupt()
        self.killsig.set()
        self.stopRetry.set()
        file_path = os.path.join(curr_dir, "memo.yaml")
        with open(file_path, 'w') as f:
            data = {"memo": self.memo,
                    "exclude": self.exclude}
            yaml.dump(data, f, default_flow_style=False)

    def parseMapCoords(self):
        image = env.capture(dofus.MAP_COORDS_R)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lower_blue = np.array([228, 220, 220])
        upper_blue = np.array([255, 230, 255])
        bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mask = cv2.inRange(bgr_img, lower_blue, upper_blue)
        result = cv2.bitwise_and(gray, gray, mask=mask)
        result = cv2.threshold(result, 0, 255, cv2.THRESH_BINARY_INV)[1]
        result = cv2.blur(result, (2, 2), 0)
        text = pytesseract.image_to_string(result, config='--psm 6')
        res = re.findall("(-?\d+),(-?\d+)", text)
        if res:
            return int(res[0][0]), int(res[0][1])
        else:
            return None




def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    env.focusDofusWindow()
    start_map = (8, -21)
    end_map = (12, -15)
    curr_map = (5, -18)
    path_to_start = [dofus.RIGHT] * 3
    fighter = FightsFarmer(start_map, end_map, path_to_start, curr=curr_map)
    atexit.register(tearDown, fighter)
    fighter.start()
    fighter.join()
    # env.focusIDEWindow()
