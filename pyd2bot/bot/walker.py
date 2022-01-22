import collections
import datetime
import logging
from threading import Timer
import threading
from time import perf_counter, sleep

from pyd2bot.logic.common.managers.playerManager import PlayerManager
from .bot import Bot 


logger = logging.getLogger("bot")
class Walker(Bot):

    def __init__(self, workdir, name="Dofus"):
        super(Walker, self).__init__(workdir, name=name)
        self.lastPos = None
        self.zone = None
        self.startZaap = None
        self.mapChanged = threading.Event()
        self.mapChangeTimeOut = 7.6
        self.tmpIgnore = []
        self.memoTime = 60* 3
    
    def moveToCell(self):
        pass
    
    def changeMap(self, direction, max_tries=3):
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < max_tries:
            self.mapChanged.clear()
            if self.moving.wait(1):
                self.idle.wait()
            if self.mapChanged.wait(2):
                self.mapChanged.clear()
                sleep(0.3)
        return False

    def moveToTargets(self, targets):
        exclude = []
        while not self.killsig.is_set():
            path = self.pathToTargets(targets, exclude)
            res = True
            for x, y in path:
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
        seen = {PlayerManager.currPos}
        queue = collections.deque([[PlayerManager.currPos]])
        while queue:
            path = queue.popleft()
            if path not in exclude and path[-1] in targets:
                return path[1:]
            for coords in self.mapNeighbors(path[-1]):
                next_path = path + [coords]
                if coords not in seen and [path[-1], coords] not in exclude:
                    queue.append(next_path)
                    seen.add(coords)
        return None

    @staticmethod
    def mapNeighbors(pos, mapId=None):
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
        self.refreshMapData()
        if self.currPos not in zone:
            self.moveToZone(zone)
        while not self.killsig.is_set():
            self.randomMapChange(zone)

    def randomMapChange(self, zone):
        dst, direction = zone[self.currPos].randDirection(self.lastPos, ignore=self.tmpIgnore)
        logger.info(f"moving to rand direction {dst}, {direction}")
        if self.changeMap(direction, max_tries=1):
            return True
        else:
            if self.disconnected.is_set():
                self.connected.wait()
            else:
                if self.currPos not in zone:
                    self.moveToZone(zone)
                zone[self.currPos].excludeMap(self.lastPos, dst)

    def run(self):
        s = perf_counter()
        sleep(1)
        while not self.killsig.is_set():
            try:
                if self.currPos not in self.zone:
                    self.goToZaap(self.startZaap)
                    self.moveToZone(self.zone)
                self.tmpIgnore.append(self.currPos)
                Timer(self.memoTime, self.onTimer).start()
                self.harvest()
                while not self.killsig.is_set():
                    if self.randomMapChange(self.zone):
                        break
            except Exception as e:
                if self.disconnected.is_set():
                    self.connected.wait(60 * 5)
                else:
                    logger.error("Fatal error!", exc_info=True)
                    self.interrupt()
                    break
        total_time = str(datetime.timedelta(seconds=perf_counter() - s))
        logger.info(f"farmed for total time: {total_time}.")
        logger.info("Goodbye cruel world!")

    def onTimer(self):
        if self.tmpIgnore:
            self.tmpIgnore.pop(0)