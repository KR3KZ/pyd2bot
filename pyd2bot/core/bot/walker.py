import collections
import datetime
import logging
import random
import re
from threading import Timer
import threading
from time import perf_counter, sleep
from unittest.mock import NonCallableMagicMock
import pyautogui
from core.exceptions import *
from core import dofus, Region, env
from core.bot import Bot
from core.bot.states import *
from network.message.msg import Msg

logger = logging.getLogger("bot")
class Walker(Bot):

    def __init__(self, workdir, name="Dofus"):
        super(Walker, self).__init__(workdir, name=name)
        self.currPos = None
        self.currMapId = None
        self.lastPos = None
        self.zone = None
        self.startZaap = None
        self.mapChanged = threading.Event()
        self.mapChangeTimeOut = 7.6
        self.tmpIgnore = []
        self.memoTime = 60* 3

    def handleMsg(self, msg: Msg):
        super().handleMsg(msg)
        if msg.msgType["name"] == "MapComplementaryInformationsDataMessage":
            self.currMapInteractiveElems  = {}
            self.currMapStatedElems = {}
            
            self.currMapData = msg.json()
            
            for ielem in self.currMapData["interactiveElements"]:
                self.currMapInteractiveElems[ielem["elementId"]] = ielem
            
            for selem in self.currMapData["statedElements"]:
                self.currMapStatedElems[selem["elementId"]] = selem    
            self.mapChanged.set()
                
        if msg.msgType["name"] == "CurrentMapMessage":
            self.currMapId = int(msg.json()["mapId"])
            self.currPos = dofus.getMapCoords(self.currMapId)
            
        elif msg.msgType["name"] == "GameMapMovementRequestMessage":
            self.moving.set()
            self.idle.clear()
            
        elif msg.msgType["name"] == "GameMapMovementConfirmMessage":
            self.moving.clear()
            self.idle.set()
                    
        elif msg.msgType["name"] == "ChatClientMultiMessage":
            pass

    def changeMap(self, direction, max_tries=3):
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < max_tries:
            currx, curry = self.currPos
            directionLocs = dofus.mapChangeLoc[direction]
            random.shuffle(directionLocs)
            for tgt in directionLocs:
                with self.lock:
                    tgt.click()
                    dofus.OUT_OF_COMBAT_R.hover()
                self.mapChanged.clear()
                if self.moving.wait(1):
                    self.idle.wait()
                if self.mapChanged.wait(2):
                    self.mapChanged.clear()
                    self.lastPos = (currx, curry)
                    sleep(0.3)
                    return True
                else:
                    dofus.OUT_OF_COMBAT_R.hover()
                    sleep(0.2)
            nbr_fails += 1
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
                
    @staticmethod
    def openBank():
        dofus.BANK_MAN_R.waitAppear(dofus.BANK_MAN_P)
        dofus.BANK_MAN_R.click()  # click on bank man
        dofus.BANK_MAN_TALK_R.waitAppear(dofus.BANK_MAN_TALK_P)
        Region(771, 737, 272, 40).click()  # click first choice
        dofus.INV_OPEN_R.waitAppear(dofus.INVENTAIRE_P)

    def refreshMapData(self):
        pyautogui.press(dofus.HAVRE_SAC_SHORTCUT)
        sleep(4)
        pyautogui.press(dofus.HAVRE_SAC_SHORTCUT)
        
    def run(self):
        env.focusDofusWindow()
        s = perf_counter()
        self.sniffer.start()
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
            
    def goToZaap(self, zaap):
        logger.info("moving to zaap: " + str(zaap['coords']))
        pyautogui.press(dofus.HAVRE_SAC_SHORTCUT)
        sleep(4)
        self.mapChanged.clear()
        dofus.HAVRE_SAC_ZAAP_R.click()
        sleep(2)
        pyautogui.write(zaap['name'])
        sleep(0.5)
        pyautogui.press("enter")
        self.mapChanged.wait(10)
        if zaap['coords'] == (20, -29):
            Region(618, 729, 36, 24).click()
            sleep(4)
        return True
