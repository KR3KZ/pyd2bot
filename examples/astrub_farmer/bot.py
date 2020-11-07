import atexit
import os
import random
from core import bot
from time import perf_counter
from core import env
from core.zone import Zone


class FightsFarmer(bot.Bot):

    def __init__(self, zone, spell, mobs_patterns, save_path):
        super(FightsFarmer, self).__init__(zone, spell, save_path, "FightsFarmer")
        self.mobs_patterns = mobs_patterns

    def run(self):
        s = perf_counter()
        nbr_farmed = 0
        self.fighter_thread.start()
        if os.path.exists(self.save_path):
            self.harvestZone.loadCache(self.save_path)
            
        self.updateMapCoords()
        while not self.killsig.is_set():
            try:
                if not self.insideZone():
                    self.moveToZone()
                self.updateMapCoords()
                nbr_farmed += self.harvestCombats(self.mobs_patterns)
                self.randomWalk()
            except Exception as e:
                logging.info(str(e))
                self.interrupt()
                break
        logging.info(f"farmed {nbr_farmed}mobs in {perf_counter() - s}seconds")
        logging.debug("Goodbye cruel world!")

    def randomWalk(self):
        while not self.killsig.is_set():
            x, y = self.currMapCoords
            key = (self.last_map, (x, y))
            logging.debug(f"Current map {(x, y)}")
            if key in self.harvestZone.cache:
                choices = self.harvestZone.neighbors(x, y) - self.harvestZone.cache[key]
            else:
                choices = self.harvestZone.neighbors(x, y)
            nx, ny = random.choice(list(choices))
            rand_direction = nx - x, ny -y
            if self.moveTo(rand_direction, nbr_retries=2):
                return True
            else:
                key = (self.last_map, (x, y))
                if key not in self.harvestZone.cache:
                    self.harvestZone.cache[key] = set()
                self.harvestZone.cache[key].add((nx, ny))


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    from core import utils
    import logging

    work_dir = os.path.dirname(os.path.abspath(__file__))
    graph_file = os.path.join(work_dir, 'cache.yaml')
    log_file = os.path.join(work_dir, 'bot.log')
    patterns_dir = os.path.join(work_dir, "mobs_patterns")
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')

    mob_patterns = utils.loadPatternsFromDir(patterns_dir)

    combat_spell = {
        "range": 6,
        "nbr": 3,
        "shortcut": "z"
    }

    top_left = (8, -21)
    bot_right = (12, -15)
    zone = Zone(top_left, bot_right)

    bot = FightsFarmer(zone, combat_spell, mob_patterns, graph_file)
    atexit.register(tearDown, bot)

    env.focusDofusWindow()
    bot.start()
    bot.join()
    env.focusIDEWindow()
