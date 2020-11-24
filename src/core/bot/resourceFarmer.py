import datetime
import logging
import os
from time import sleep
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

    def harvest(self):
        logging.debug("Searching for resources...")
        currMap = self.zone[self.currPos]
        currMap['nbrseen'] += 1
        if currMap['nbrseen'] > 25:
            currMap['nbrseen'] = 0
            currMap['excludedMaps'] = {}
            currMap['excludedSpots'] = {}
        self.collectLearnedSpots()
        if currMap['nbrseen'] < 10:
            self.discoverSpots()

    def collectLearnedSpots(self):
        currMap = self.zone[self.currPos]
        for spot in currMap['spots']:
            if spot['region'].find(spot['pattern']['bi'], threshold=0.7):
                if currMap.isValidSpot(self.lastPos, spot):
                    if not self.collect(spot):
                        currMap.excludeSpot(self.lastPos, spot)
        if self.combatStarted.is_set():
            self.combatEnded.wait()
        if self.disconnected.is_set():
            self.connected.wait()

    def discoverSpots(self):
        seen = []
        currMap = self.zone[self.currPos]
        while not self.killsig.is_set():
            matched = False
            for kind, patterns in self.patterns.items():
                pattern_imgs = [p['bi'] for p in patterns]
                tgt, idx = dofus.COMBAT_R.findAny(pattern_imgs, threshold=0.7)
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
