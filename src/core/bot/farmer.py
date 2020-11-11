import datetime
import logging
import os
from time import perf_counter
import yaml
from core.bot import Fighter
from core import dofus


class MobsFarmer(Fighter):

    def __init__(self, zone, spell, mobs_patterns, save_path):
        super(MobsFarmer, self).__init__(spell, name="MobsFarmer")
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


class ResourceFarmer(Fighter):

    def __init__(self, data, spell, mobs_patterns):
        super(ResourceFarmer, self).__init__(spell, name="ResourceFarmer")
        self.patterns = [[_, 0] for _ in mobs_patterns]
        self.nbr_no_farm = {}
        self.currStep = 0
        self.startMap = tuple(map(int, data['start-map']))
        self.path = self.buildPath(data['path'])

    def buildPath(self, data):
        directionD = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
        path = [self.startMap]
        for step in data:
            currx, curry = path[-1]
            dx, dy = directionD[step]
            nextStep = currx + dx, curry + dy
            path.append(nextStep)
        return path

    def run(self):
        super(ResourceFarmer, self).run()
        s = perf_counter()
        nbr_farmed = 0

        try:

            self.updatePos()
            if self.currPos != self.startMap:
                self.moveToMap(self.startMap)

            while not self.killsig.is_set():
                self.updatePos()
                self.patterns.sort(key=lambda it: it[1])
                result = self.harvestResources([p for p, s in self.patterns])
                for idx, score in result['matched'].items():
                    self.patterns[idx][1] += score
                self.nextStep()

        except Exception as e:
            logging.error("Fatal error!", exc_info=True)
            if self.disconnected.wait(10):
                self.connected.wait()
            else:
                self.interrupt()

        total_time = str(datetime.timedelta(seconds=perf_counter() - s))
        logging.info(f"farmed {nbr_farmed}mobs in {total_time}.")
        logging.info("Goodbye cruel world!")

    def nextStep(self):
        nx, ny = self.path[self.currStep + 1]
        x, y = self.currPos
        direction = nx - x, ny - y
        self.changeMap(direction)
        self.currStep = self.currStep + 1

    def harvestResources(self, patterns):
        result = {
            "farmed": 0,
            "matched": {}
        }
        while not self.killsig.is_set():
            tgt, idx = dofus.COMBAT_R.findAny(patterns, threshold=0.7)
            if not tgt:
                break
            tgt.click()
            tgt.waitChange(1)
            tgt.waitChange(9)
            result['farmed'] += 1
            if idx not in result['matched']:
                result['matched'][idx] = 0
            result['matched'][idx] += 1
            if self.combatStarted.is_set():
                self.combatEnded.wait()
        return result

    def interrupt(self):
        super(ResourceFarmer, self).interrupt()