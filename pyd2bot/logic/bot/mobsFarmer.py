import datetime
import logging
import os
from time import perf_counter
import yaml
from core.bot import Fighter


class MobsFarmer(Fighter):

    def __init__(self, zone, spell, mobs_patterns, save_path, name):
        super(MobsFarmer, self).__init__(spell, name=name)
        self.mobs_patterns = [[_, 0] for _ in mobs_patterns]
        self.nbr_no_farm = {}
        self.cache = {}
        self.save_path = save_path
        self.zone = zone

    def run(self):
        super(MobsFarmer, self).run()
        s = perf_counter()
        nbr_farmed = 0
        self.loadCache()
        self.updatePos()

        while not self.killsig.is_set():
            try:
                if self.currPos not in self.zone:
                    self.moveToZone(self.zone)
                self.updatePos()
                self.mobs_patterns.sort(key=lambda it: it[1])
                result = self.harvestCombats([p for p, s in self.mobs_patterns])
                self.zone[self.currPos]['farmed'] += result['farmed']
                for idx, score in result['matched'].items():
                    self.mobs_patterns[idx][1] += score
                self.randomWalk(self.zone)
            except Exception as e:
                if self.disconnected.is_set():
                    self.connected.wait()
                else:
                    logging.error("Fatal error!", exc_info=True)
                    self.interrupt()
                    break

        total_time = str(datetime.timedelta(seconds=perf_counter() - s))
        logging.info(f"farmed {nbr_farmed}mobs in {total_time}.")
        logging.info("Goodbye cruel world!")

    def interrupt(self):
        self.saveCache()
        super(MobsFarmer, self).interrupt()

    def loadCache(self):
        if os.path.exists(self.save_path):
            with open(self.save_path, 'r') as f:
                self.cache = yaml.load(f, Loader=yaml.FullLoader)

    def saveCache(self):
        with open(self.save_path, 'w') as f:
            yaml.dump(self.cache, f)
