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
        self.farming = threading.Event()
        self.farmingError = threading.Event()
        self.currFarmingElem = None


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
        while not self.killsig.is_set():
            self.currFarmingElem = None
            try:
                logger.info("looking for collectable resources")
                for elem_id in self.currMapInteractiveElems.keys():         
                    if self.canCollect(elem_id):
                        selem = self.currMapStatedElems[elem_id]
                        logger.info(f"Collecting elem {elem_id}")
                        cell_id = selem["elementCellId"]
                        self.farming.clear()
                        self.moving.clear()
                        x, y = dofus.getCellCoords(cell_id)
                        px, py = dofus.getCellPixelCenterCoords(x, y)
                        for _ in range(3):
                            env.shiftClick(px, py)
                            dofus.OUT_OF_COMBAT_R.hover()
                            if self.moving.wait(1):
                                while self.moving.is_set():sleep(0.1)
                            if self.farming.wait(1):
                                while self.farming.is_set():sleep(0.1)
                                break
                        if self.farmingError.is_set():
                            # handle collect errors here
                            logger.info("Unable to collect the resource")
                        if self.fullPodsAAA.is_set():
                            logger.info("Warning pods reached more than 90% of total capacity")
                        if self.isInFight.is_set():
                            logger.info("Combat started")
                            self.onCombatStarted()
                            while self.context != 1:
                                sleep(0.1)
                            sleep(3)
                            pyautogui.press("escape")
                        if self.mapChanged.is_set():
                            self.mapChanged.clear()
                            raise MapChangedWhileFarmingError
                        if self.killsig.is_set():
                            return
                return
            except MapChangedWhileFarmingError:
                logger.info("Bot missclicked and changed map while farming, will repeat harvest on new map")
                
    def interrupt(self):
        data = self.zone.toDict()
        with open(self.today_save_file, 'w') as f:
            yaml.dump(data, f, sort_keys=False)
        super(ResourceFarmer, self).interrupt()