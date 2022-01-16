import datetime
import logging
import os
import threading
from time import sleep
import math
import pyautogui
import yaml
from core.bot import Fighter
from core.bot.states import *
from core import dofus, env
import json
from network.message.msg import Msg
import random

class MapChangedWhileFarmingError(Exception):
    pass

logger = logging.getLogger("bot")
class ResourceFarmer(Fighter):

    def __init__(self, zone, zaap, spell, workdir, name):
        super(ResourceFarmer, self).__init__(spell, workdir, name=name)
        self.zone = zone
        self.startZaap = zaap
        now = datetime.datetime.now()
        self.save_dir = os.path.join(self.workdir, 'saves')
        save_file_name = self.zone.name.replace(' ', '_') + '_' + now.strftime("%d_%m_%Y") + ".yaml"
        self.today_save_file = os.path.join(self.save_dir, save_file_name)
        self.farmingStarted = threading.Event()
        self.farmingEnded = threading.Event()
        self.farmingError = threading.Event()
        self.currFarmingElem = None

    def handleMsg(self, msg: Msg):
        super().handleMsg(msg)
        
        if msg.msgType["name"] == "InteractiveUseErrorMessage":
            self.farmingError.set()
        
        if msg.msgType["name"] == "InteractiveUsedMessage":
            logger.info("Got message telling farm started")
            self.farmingStarted.set()
        
        elif msg.msgType["name"] == "InteractiveUseEndedMessage":
            logger.info("Got message telling farm ended")
    
        elif msg.msgType["name"] == "StatedElementUpdatedMessage":
            msg_json = msg.json()
            elem_id = msg_json["statedElement"]["elementId"]
            self.currMapStatedElems[elem_id] = msg_json["statedElement"]
        
        elif msg.msgType["name"] == "InteractiveElementUpdatedMessage":
            msg_json = msg.json()
            elem_id = msg_json["interactiveElement"]["elementId"]
            logger.info("received interaction update for elem: " + str(elem_id))
            if self.currFarmingElem == elem_id:
                self.farmingStarted.clear()
                self.farmingEnded.set()
                self.currFarmingElem = None
            self.currMapInteractiveElems[elem_id] = msg_json["interactiveElement"]
        
        elif msg.msgType["name"] == "GameFightStartingMessage":
            self.combatStarted.set()
            
    def harvest(self):
        logger.info("harvest called")
        self.collect()
        self.checkPopup()

    def canCollect(self, elem_id):
        ielem = self.currMapInteractiveElems[elem_id]
        selem = self.currMapStatedElems[elem_id]
        if ielem["onCurrentMap"] and selem["elementState"] == 0 and ielem["enabledSkills"]:
            return True
        return False
                
    def collect(self):
        logger.info("looking for collectable resources")
        while not self.killsig.is_set():
            try:
                for elem_id in self.currMapInteractiveElems.keys():
                    for _ in range(6):
                        if self.canCollect(elem_id):
                            self.currFarmingElem = None
                            ielem = self.currMapInteractiveElems[elem_id]
                            selem = self.currMapStatedElems[elem_id]
                            logger.info("collecting elem state : " + str(selem))
                            logger.info("collecting elem interactions : " + str(ielem))
                            cell_id = selem["elementCellId"]
                            self.farmingStarted.clear()
                            self.farmingEnded.clear()
                            self.moving.clear()
                            x, y = dofus.getCellCoords(cell_id)
                            px, py = dofus.getCellPixelCenterCoords(x, y)
                            pyautogui.keyDown('shift')
                            sleep(0.1)
                            map_px, map_py, map_pw, map_ph = dofus.COMBAT_R.getRect()
                            cell_w = int(map_pw / (2 * dofus.HCELLS)) 
                            cell_h = int(map_ph / (2 * dofus.VCELLS)) 
                            rand_px = px + random.randint(-cell_w//3, cell_w//3)
                            rand_py = py + random.randint(-cell_h//3, cell_h//3)
                            env.click(rand_px, rand_py)
                            sleep(0.1)
                            pyautogui.keyUp('shift')
                            dofus.OUT_OF_COMBAT_R.hover()
                            if self.moving.wait(1):
                                self.idle.wait()
                            if self.farmingStarted.wait(1):
                                logger.info("got farming started event")
                                self.currFarmingElem = elem_id
                                self.farmingEnded.wait()
                                logger.info("got farming ended event")
                                self.farmingEnded.clear()
                                break
                            if self.farmingError.is_set():
                                logger.info("Unable to collect the resource")
                            if self.fullPodsAAA.is_set():
                                logger.info("Warning pods reached 90% of total capacity")
                            if self.combatStarted.is_set():
                                logger.info("Combat started")
                                self.combatEnded.wait()
                            if self.mapChanged.is_set():
                                self.mapChanged.clear()
                                raise MapChangedWhileFarmingError
                return
            except MapChangedWhileFarmingError:
                logger.info("Bot missclicked and changed map while farming, will repeat harvest on new map")
            
            
    def interrupt(self):
        data = self.zone.toDict()
        with open(self.today_save_file, 'w') as f:
            yaml.dump(data, f, sort_keys=False)
        super(ResourceFarmer, self).interrupt()