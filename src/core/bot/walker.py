import collections
import logging
from time import perf_counter
from core.exceptions import *
from core import env, dofus
from core.bot import Bot


class Walker(Bot):

    def __init__(self, name="Walker"):
        super(Walker, self).__init__(name=name)
        self.currPos = None
        self.lastPos = None

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
            with self.lock:
                dofus.mapChangeLoc[direction].click()
                dofus.COMBAT_R.hover()
            if self.waitMapChange(dstx, dsty):
                self.lastPos = (currx, curry)
                return True
            nbr_fails += 1
        return False

    def waitMapChange(self, x, y, timeout=7.5):
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
                if not self.changeMap(direction, max_tries=1):
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
            dst, direction = zone[self.currPos].randDirection(self.lastPos)
            if self.changeMap(direction, max_tries=2):
                return True
            else:
                zone[self.currPos].exclude(self.lastPos, dst)
