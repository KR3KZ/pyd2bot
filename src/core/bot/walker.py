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
        self.startZaap = NonCallableMagicMock
        self.posRequestState = PosRequestState.idle
        self.mapChanged = threading.Event()
        self.mapChangeTimeOut = 7.6
        self.tmpIgnore = []
        self.memoTime = 60 * 15

    def handleMsg(self, msg: Msg):
        super().handleMsg(msg)
        if msg.msgType["name"] == "MapComplementaryInformationsDataMessage":
            logger.info("got new map infos")
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
            logger.info("got movement started msg")
            self.moving.set()
            self.idle.clear()
            
        elif msg.msgType["name"] == "GameMapMovementConfirmMessage":
            logger.info("got movement ended msg")
            self.moving.clear()
            self.idle.set()
                    
        elif msg.msgType["name"] == "ChatClientMultiMessage":
            if self.posRequestState == PosRequestState.msgSent:
                msg_json = msg.json()
                if msg_json["channel"] == 0:
                    m = re.match(".*{map,(-?\d+),(-?\d+),1}.*", msg_json["content"])
                    if m:
                        x = int(m.group(1))
                        y = int(m.group(2))
                        self.currPos = (x, y)
                        self.posRequestState = PosRequestState.gotResponse

            
    def getCurrPos(self):
        pyautogui.press('space')
        pyautogui.write("%pos%")
        self.posRequestState = PosRequestState.msgSent
        pyautogui.press('enter')
        if self.waitPosMsg(20):
            return self.currPos
        return None
    
    def changeMap(self, direction, max_tries=3):
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < max_tries:
            currx, curry = self.currPos
            dstx, dsty = currx + direction[0], curry + direction[1]
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
                    self.lastPos = (currx, curry)
                    sleep(0.3)
                    return True
                else:
                    dofus.OUT_OF_COMBAT_R.hover()
                    sleep(0.2)
        nbr_fails += 1
        return False

    def waitPosMsg(self, t=20):
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < t:
            if self.posRequestState == PosRequestState.gotResponse:
                self.posRequestState = PosRequestState.idle
                return True
            sleep(0.1)
        return False
                 
    def waitMapChange(self, x, y, timeout=20):
        logger.debug(f"Current map coords: {self.currPos}")
        logger.debug(f"Changing map to destination ({x}, {y})")
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < timeout:
            if self.combatStarted.wait(0.3):
                self.combatEnded.wait()
            if self.mapChangeState == MapChangeState.done:
                logger.debug(f"Change map took {perf_counter() - s}")
                self.mapChangeState = MapChangeState.idle
                return True
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
        self.getCurrPos()
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
                self.getCurrPos()
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

    def refreshMapData():
        pyautogui.press(dofus.HAVRE_SAC_SHORTCUT)
        pyautogui.press(dofus.HAVRE_SAC_SHORTCUT)
        
    def run(self):
        self.disconnectedObs.start()
        env.focusDofusWindow()
        s = perf_counter()
        self.sniffer.start()
        sleep(1)
        self.getCurrPos()
        while not self.killsig.is_set():
            try:
                if self.currPos not in self.zone:
                    self.goToZaap(self.startZaap)
                    self.moveToZone(self.zone)
                self.tmpIgnore.append(self.currPos)
                Timer(self.memoTime, self.onTimer).start()
                self.harvest()
                if self.combatStarted.is_set():
                    self.combatEnded.wait()
                self.randomMapChange(self.zone)
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
        pyautogui.press("escape")
        sleep(1)
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
