import atexit
import datetime
import os
import threading
import random

import cv2
import yaml

from core.fighter import Fighter
from core.log import Log
from core.utils import retry
from core import env, dofus

log = Log()
curr_dir = os.path.dirname(os.path.abspath(__file__))

class FightsFarmer(threading.Thread):
    UP = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DOWN = (0, 1)

    def __init__(self, startMap, endMap, curr=None, exclude=None):
        threading.Thread.__init__(self, name='FightFarmer')
        if exclude is None:
            exclude = set()
        if not curr:
            curr = startMap
        self.stopSignal = threading.Event()
        self.stopRetry = threading.Event()
        self.lock = threading.Lock()
        self.fighter_thread = Fighter(dofus.SOURNOISERIE, parent=self)
        self.currMap = curr
        self.endMap = endMap
        self.startMap = startMap
        self.memo = {}
        self.exclude = exclude

    def inZone(self, mapCoords):
        mapx, mapy = mapCoords
        return self.startMap[0] <= mapx <= self.endMap[0] and \
               self.startMap[1] <= mapy <= self.endMap[1]

    def randNextMap(self):
        moves = {self.UP, self.DOWN, self.LEFT, self.RIGHT}
        while not self.stopSignal.is_set():
            move = random.choice(list(moves - self.memo[self.currMap]))
            nextMap = self.currMap[0] + move[0], self.currMap[1] + move[1]
            if nextMap not in self.exclude and self.inZone(nextMap):
                return move, nextMap
            else:
                self.memo[self.currMap].add(move)

    def run(self):
        self.loadMemo()
        self.fighter_thread.start()
        while not self.stopSignal.is_set():
            try:
                log.info(f"current map {self.currMap}")
                if not self.findCombat(reraise=False, nbr_retries=3):
                    log.info("I will exclude {self.currMap}")
                    self.exclude.add(self.currMap)
                else:
                    self.fighter_thread.combatEnded.wait()
                self.randomWalk()
            except Exception as e:
                log.info(exc_info=True)
                self.interrupt()
        log.info("Goodbye cruel world!")

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
        while not self.stopSignal.is_set():
            direction, nextMap = self.randNextMap()
            res, info = self.changeMap(direction, nextMap)
            if res:
                break
            elif info == "TIMEOUT":
                self.memo[self.currMap].add(direction)

    @retry
    def findCombat(self):
        while not self.stopSignal.is_set():
            tgt = dofus.COMBAT_R.findAny(dofus.mobs, threshold=0.75, shuffle=True)
            if tgt:
                log.info("I found a mob group")
                self.enterCombat(tgt, nbr_retries=2)
                self.fighter_thread.combatEnded.wait()
            else:
                log.info("Didn't find any mobs here")
                return 1

    @retry
    def enterCombat(self, tgt, timeout=4):
        with self.lock:
            tgt.click()
            log.info("clicked on mobs group")
        if self.fighter_thread.combatDetected.wait(timeout):
            return
        log.info("couldn't open combat!")
        raise TimeoutError("enter combat timed out!")

    def changeMap(self, direction, nextMap, timeout=12):
        log.info(f"changing map to {nextMap}")
        with self.lock:
            if direction == self.DOWN:
                dofus.MAP_DOWN_L.click()
            elif direction == self.UP:
                dofus.MAP_UP_L.click()
            elif direction == self.LEFT:
                dofus.MAP_LEFT_L.click()
            elif direction == self.RIGHT:
                dofus.MAP_RIGHT_L.click()
        if dofus.MINIMAP_R.waitChange(timeout):
            if self.fighter_thread.combatDetected.wait(0.2):
                return False, "AGRO"
            self.currMap = nextMap
            return True, ""
        return False, "TIMEOUT"

    def interrupt(self):
        log.info(f"I farmed {self.fighter_thread.nbr_fights} fights")
        self.fighter_thread.interrupt()
        self.stopSignal.set()
        self.stopRetry.set()
        file_path = os.path.join(curr_dir, "memo.yaml")
        with open(file_path, 'w') as f:
            data = {"memo": self.memo,
                    "exclude": self.exclude}
            yaml.dump(data, f, default_flow_style=False)


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    env.focusDofusWindow()
    fighter = FightsFarmer((8, -21), (12, -15), curr=(10, -18), exclude={(10, -19)})
    atexit.register(tearDown, fighter)
    fighter.start()
    fighter.join()
    # env.focusIDEWindow()
