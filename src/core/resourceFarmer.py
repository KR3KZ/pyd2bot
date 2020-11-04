import threading
from src.core.old_fighter import Fighter
import src.core.env as env
from .log import Log
lock = threading.Lock()
log = Log()


class Farmer(threading.Thread):

    def __init__(self, resource_pattern, src_path, nbr_cycles=1, start_step=0, max_pods=18000, min_pods=2000):
        threading.Thread.__init__(self, name='Farmer')
        self.stopSignal = threading.Event()
        self.resource_pattern = resource_pattern
        self.src_path = src_path
        self.curr_step = start_step
        self.nbr_cycles = nbr_cycles
        self.fighter_thread = Fighter(nbr_pm=5, spell=env.SOURNOISERIE, scan_rate=3)
        self.max_pods = 2071
        self.farm_path = self.loadFarmPath(self.src_path)
        self.curr_pods = min_pods

    def changeMap(self, tgt):
        log.info('changing map...')
        while not self.stopSignal.is_set():
            with lock:
                tgt.click()
            if waitVanish(env.MINIMAP_R):
                log.info("map changed")
                break

    def collectResource(self):
        rtype, rregion = self.farm_path[self.curr_step]
        rpattern = self.resource_pattern[rtype]
        match = rregion.findBest(rpattern)
        if match:
            rregion.hover()
            sleep(0.3)
            current = Pattern(capture(rregion))
            rregion.click()
            waitForChange(rregion)
            rregion.waitVanish(current.similar(0.6))
            return True
        return False

    def run(self):
        self.fighter_thread.start()
        path_length = len(self.farm_path)
        cycle = 0
        while not self.stopSignal.is_set() and cycle < self.nbr_cycles:

            while not self.stopSignal.is_set() and self.curr_step < path_length:

                if self.fighter_thread.combatDetected.waitAppear(0.5):
                    log.info('waiting for fighter to end...')
                    self.fighter_thread.combatEnded.waitAppear()
                    self.curr_step -= 1

                log.info('step number ' + str(self.curr_step) + ' ...')
                rtype, rregion = self.farm_path[self.curr_step]
                self.curr_step += 1

                if rtype != 'mapChange':
                    self.collectResource()

                else:
                    self.changeMap()

            if not self.stopSignal.is_set():
                cycle += 1
                self.curr_step = 0
                wait(2)
                with lock:
                    useRappelPotion()
                sleep(2)
                log.info('cycle number' + str(cycle) + 'ended')

        self.fighter_thread.interrupt()
        log.info('farmer stopped')

    def interrupt(self):
        self.fighter_thread.interrupt()
        self.stopSignal.set()

    @staticmethod
    def loadFarmPath(src_path):
        with open(src_path) as file:
            result = []
            for line in file:
                if line and line != '\n' and not line.startswith("#"):
                    data_list = line.split(',')
                    rtype = data_list[0]
                    rec = [int(e.strip('\n')) for e in data_list[1:]]
                    resource_region = QRect(*rec)
                    result.append((rtype, resource_region))
        return result
