import collections
import datetime
import logging
import random
import re
from threading import Timer
import threading
from time import perf_counter, sleep
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
        self.tmpIgnore = []
        self.zone = None
        self.startZaap = None
        self.memoTime = 60 * 15
        self.mapChangeState = MapChangeState.idle
        self.posRequestState = PosRequestState.idle
        self.moving = threading.Event()
        self.mapChangeTimeOut = 7.6
        
    def handleMsg(self, msg: Msg):
        if msg.msgType["name"] == "MapComplementaryInformationsDataMessage":
            self.mapChangeState = MapChangeState.done
            self.currMapData = msg.json()
            
        if msg.msgType["name"] == "CurrentMapMessage":
            map_id = int(msg.json()["mapId"])
            self.currPos = dofus.getMapCoords(map_id)
            self.mapChangeState = MapChangeState.done
        
        if msg.msgType["name"] == "GameMapMovementRequestMessage":
            self.moving.set()
            if self.mapChangeState == MapChangeState.clicked:
                self.mapChangeState = MapChangeState.moving
            
        if msg.msgType["name"] == "GameMapMovementConfirmMessage":
            self.moving.clear()
                    
        if msg.msgType["name"] == "ChatClientMultiMessage":
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
        return self.waitPosMsg(20)
    
    def changeMap(self, direction, max_tries=3):
        nbr_fails = 0
        while not self.killsig.is_set() and nbr_fails < max_tries:
            currx, curry = self.currPos
            dstx, dsty = currx + direction[0], curry + direction[1]
            directionLocs = dofus.mapChangeLoc[direction]
            random.shuffle(directionLocs)
            for tgt in directionLocs:
                with self.lock:
                    self.shiftClick(tgt)
                self.mapChangeState = MapChangeState.clicked
                if self.moving.wait(1):
                    if self.waitMapChange(dstx, dsty, self.mapChangeTimeOut):
                        self.lastPos = (currx, curry)
                        return True
                    else:
                        dofus.OUT_OF_COMBAT_R.click()
                        sleep(0.2)
            nbr_fails += 1
        return False

    def waitPosMsg(self, t=20):
        s = perf_counter()
        while not self.killsig.is_set() and perf_counter() - s < t:
            if self.posRequestState == PosRequestState.gotResponse:
                self.posRequestState = PosRequestState.idle
                return True
            sleep(0.2)
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
                if self.currPos != (x, y):
                    raise Exception(f"Landed on the wrong map {self.currPos} when requested to go to map {(x, y)}")
                return True
        return False

    def moveToTargets(self, targets):
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
    def mapNeighbors(pos, mapId=None):
        directions = dofus.getMapDirections(mapId)
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

    @staticmethod
    def openBank():
        dofus.BANK_MAN_R.waitAppear(dofus.BANK_MAN_P)
        dofus.BANK_MAN_R.click()  # click on bank man
        dofus.BANK_MAN_TALK_R.waitAppear(dofus.BANK_MAN_TALK_P)
        Region(771, 737, 272, 40).click()  # click first choice
        dofus.INV_OPEN_R.waitAppear(dofus.INVENTAIRE_P)

    def run(self):
        if not self.resourcesToFarm:
            self.resourcesToFarm = self.patterns.keys()
        self.disconnectedObs.start()
        env.focusDofusWindow()
        s = perf_counter()
        self.sniffUi.start()
        self.updatePos()

        while not self.killsig.is_set():
            env.focusDofusWindow()
            try:
                if self.fullPods():
                    self.discharge()
                if self.currPos not in self.zone:
                    self.goToZaap(self.startZaap)
                    self.moveToZone(self.zone)
                self.tmpIgnore.append(self.currPos)
                Timer(self.memoTime, self.onTimer).start()
                self.harvest()
                if self.combatStarted.is_set():
                    self.combatEnded.wait()
                self.randomWalk(self.zone)
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

    def goToZaap(self, zaap):
        logger.info("moving to zaap: " + str(zaap['coords']))
        pyautogui.press(dofus.HAVRE_SAC_SHORTCUT)
        sleep(4)
        dofus.HAVRE_SAC_ZAAP_R.click()
        sleep(2)
        Region(1116, 230, 21, 14).click()
        pyautogui.write(zaap['name'])
        Region(910, 757, 105, 16).click()
        self.waitMapChange(*zaap['coords'], 60 * 15)
        if zaap['coords'] == (20, -29):
            Region(618, 729, 36, 24).click()
            sleep(4)
        return True
