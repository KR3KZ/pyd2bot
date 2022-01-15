import datetime
import logging
import os
from time import sleep
import math
import pyautogui
import yaml
from core.bot import Fighter
from core import dofus, env
import json

class ResourceFarmer(Fighter):

    def __init__(self, zone, zaap, spell, workdir, name):
        super(ResourceFarmer, self).__init__(spell, workdir, name=name)
        self.zone = zone
        self.startZaap = zaap
        now = datetime.datetime.now()
        self.save_dir = os.path.join(self.workdir, 'saves')
        save_file_name = self.zone.name.replace(' ', '_') + '_' + now.strftime("%d_%m_%Y") + ".yaml"
        self.today_save_file = os.path.join(self.save_dir, save_file_name)
        self.famPatternThreshold = 0.7

    def harvest(self):
        logging.debug("Searching for resources...")
        self.collect()
        self.checkPopup()

    def collect(self):
        with open("map.json", 'r') as fp:
            map_data = json.load(fp)
            stated_elems = {}
            for ele in map_data["statedElements"]:
                stated_elems[ele["elementId"]] = ele
            for iele in map_data["interactiveElements"]:
                if iele["onCurrentMap"]:
                    sele = stated_elems[iele["elementId"]]
                    if sele["elementState"] == 0:
                        x, y = self.getCellCoords(sele["elementCellId"])
                        env.focusDofusWindow()
                        px, py = self.getCellPixelCenterCoords(x, y)
                        pyautogui.keyDown('shift')
                        env.click(px, py)
                        pyautogui.keyUp('shift')
                        dofus.OUT_OF_COMBAT_R.hover()
                
    def interrupt(self):
        data = self.zone.toDict()
        with open(self.today_save_file, 'w') as f:
            yaml.dump(data, f, sort_keys=False)
        super(ResourceFarmer, self).interrupt()
