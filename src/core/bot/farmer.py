import datetime
import logging
import os
import random
import threading
from time import perf_counter
import yaml
from core import Observer, dofus
from core.bot import Fighter, Walk


class MobsFarmer(threading.Thread):

    def __init__(self, zone, spell, mobs_patterns, save_path):
        threading.Thread.__init__(self, name="FightsFarmer")
        self.killsig = threading.Event()
        self.disconnected = threading.Event()
        self.connected = threading.Event()
        self.mobs_patterns = [[_, 0] for _ in mobs_patterns]
        self.nbr_no_farm = {}
        self.cache = {}
        self.save_path = save_path
        self.harvestZone = zone
        self.fighter = Fighter(spell, parent=self)
        self.walk = Walk(self)
        self.disconnectedObs = Observer(dofus.CONNECT_R,
                                        dofus.DISCONNECTED_BOX_P,
                                        self.reconnect,
                                        Observer.Mode.APPEAR,
                                        rest_time=5)

    def run(self):
        s = perf_counter()
        nbr_farmed = 0
        self.fighter.start()
        self.disconnectedObs.start()
        self.loadCache()
        self.walk.updateCoords()
        while not self.killsig.is_set():
            try:

                if not self.harvestZone.inside(*self.walk.coordinates):
                    self.walk.moveToZone(self.harvestZone)

                self.walk.updateCoords()

                self.mobs_patterns.sort(key=lambda it: it[1])

                result = self.fighter.harvestCombats([p for p, s in self.mobs_patterns])

                nbr_farmed += result['farmed']

                for idx, score in result['matched'].items():
                    self.mobs_patterns[idx][1] += score

                self.updateFarmTrack(nbr_farmed)

                self.randomWalk()

            except Exception:
                if self.disconnected.wait(20):
                    self.connected.wait()
                else:
                    logging.error("Fatal error!", exc_info=True)
                    self.interrupt()
                    break

        total_time = str(datetime.timedelta(seconds=perf_counter() - s))
        logging.info(f"farmed {nbr_farmed}mobs in {total_time}.")
        logging.info("Goodbye cruel world!")

    def updateFarmTrack(self, nbr_farm):
        currMap = self.walk.coordinates
        if nbr_farm == 0:
            if currMap not in self.nbr_no_farm:
                self.nbr_no_farm[currMap] = 0
            self.nbr_no_farm[currMap] += 1
        else:
            if self.walk.coordinates in self.nbr_no_farm:
                self.nbr_no_farm[currMap] = 0

    def randomWalk(self):
        while not self.killsig.is_set():
            x, y = self.walk.coordinates
            currMapNeighbors = self.harvestZone.neighbors(x, y)
            key = (self.walk.lastMap, (x, y))
            non_farmable = {m for m, val in self.nbr_no_farm.items() if val >= 5}
            choices = currMapNeighbors - non_farmable
            if key in self.cache:
                choices = choices - self.cache[key]
            if not choices:
                choices = currMapNeighbors

            nx, ny = random.choice(list(choices))
            rand_direction = nx - x, ny - y
            if self.walk.changeMap(rand_direction, max_tries=2):
                return True
            else:
                key = (self.walk.lastMap, (x, y))
                if key not in self.cache:
                    self.cache[key] = set()
                self.cache[key].add((nx, ny))

    def interrupt(self):
        self.disconnectedObs.stop()
        self.harvestZone.saveTo(self.save_path)
        self.fighter.interrupt()

    def reconnect(self):
        logging.info("Disconnected popup appeared!")
        self.disconnected.set()
        self.connected.clear()
        dofus.CLOSE_DISCONNECTED_BOX_L.click()
        dofus.CONNECT_R.waitVanish(dofus.DISCONNECTED_BOX_P)
        dofus.RECONNECT_BUTTON_R.click()
        dofus.PLAY_GAME_BUTTON_R.waitAppear(dofus.PLAY_GAME_BUTTON_P)
        dofus.PLAY_GAME_BUTTON_R.click()
        while not self.walk.parseMapCoords():
            pass
        self.disconnected.clear()
        self.connected.set()

    def loadCache(self):
        if os.path.exists(self.save_path):
            with open(self.save_path, 'r') as f:
                self.cache = yaml.load(f, Loader=yaml.FullLoader)

    def saveCache(self):
        with open(self.save_path, 'w') as f:
            yaml.dump(self.cache, f)