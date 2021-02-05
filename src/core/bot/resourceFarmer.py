import datetime
import logging
import os
from time import sleep

import pyautogui
import yaml
from core.bot import Fighter
from core import dofus


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
        currMap = self.zone[self.currPos]

        if currMap['nbrseen'] > 30:
            currMap['nbrseen'] = 9

        if currMap['nbrseen'] < 10:
            self.discoverSpots()

        else:
            self.collectLearnedSpots()

        currMap['nbrseen'] += 1
        self.checkPopup()

    def collectLearnedSpots(self):
        currMap = self.zone[self.currPos]
        for spot in currMap['spots']:
            if spot['pattern']['kind'] in self.resourcesToFarm and \
                    spot['region'].find(spot['pattern']['bi'], threshold=0.8):
                if currMap.isValidSpot(self.lastPos, spot):
                    self.collect(spot)

    def discoverSpots(self):
        seen = []
        currMap = self.zone[self.currPos]
        while not self.killsig.is_set():
            matched = False
            for kind in self.resourcesToFarm:
                patterns = self.patterns[kind]
                pattern_imgs = [p['bi'] for p in patterns]
                tgt, idx = dofus.COMBAT_R.findAny(pattern_imgs, threshold=self.famPatternThreshold)
                if tgt and tgt not in seen:
                    spot = {
                        'region': tgt,
                        'pattern': patterns[idx]
                    }
                    seen.append(tgt)
                    res = self.collect(spot)
                    if res:
                        sleep(0.3)
                    if res and not currMap.hasSpot(spot):
                        currMap['spots'].append(spot)
                    else:
                        dofus.OUT_OF_COMBAT_R.click()
                    matched = True
            if self.combatStarted.is_set():
                self.combatEnded.wait()
            if self.disconnected.is_set():
                self.connected.wait()
            elif not matched:
                return

    def interrupt(self):
        data = self.zone.toDict()
        with open(self.today_save_file, 'w') as f:
            yaml.dump(data, f, sort_keys=False)
        super(ResourceFarmer, self).interrupt()
