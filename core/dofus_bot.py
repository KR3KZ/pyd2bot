# from sikuli.Sikuli import Region, Location, Pattern, capture, wait, FindFailed, Key, Settings
from sikuli.Sikuli import *
import threading
import atexit
import frighost_fish as frifri
from core import Grid
import os
from time import sleep
import traceback
import logging
from math import sqrt

lock = threading.Lock()





log = Log()

# Regions
MAP_R = Region(2, 29, 1918, 1002)
MINIMAP_R = Region(62, 876, 190, 122)
COMBAT_R = Region(335, 29, 1253, 885)
PM_R = Region(793, 993, 27, 34)
PA_R = Region(729, 983, 55, 42)
COMBAT_ENDED_POPUP_R = Region(841, 701, 244, 66)
READY_R = Region(1312, 925, 145, 66)
SKIP_TURN_R = Region(1312, 925, 145, 66)
COMBAT_ENDED_POPUP_CLOSE_R = Region(1231, 721, 22, 18)
MY_TURN_CHECK_R = Region(841, 1009, 17, 8)
OUT_OF_COMBAT_R = Region(104, 749, 37, 37)

# Patterns
READY_BUTTON_P = Pattern("READY_BUTTON_P.png")
COMBAT_ENDED_POPUP_P = "END_COMBAT_P.png"
SKIP_TURN_BUTTON_P = "YOUR_TURN_P.png"

# Env Vars
HCELLS = 14.5
VCELLS = 20.5
MY_TURN_COLOR = Color(252, 200, 0)
DU = (-1, -1)
DL = (-1, 1)
DD = (1, 1)
DR = (1, -1)

# Locations
MY_TURN_CHECK_L = Location(1431, 965)
END_COMBAT_CLOSE_L = Location(1240, 728)

# Timers
CHANGE_MAP_TIMEOUT = 3 * 60

# Shortcuts
RAPPEL_POTION_SHORTCUT = "e"

# Spells
SOURNOISERIE = {
    "shortcut": "z",
    "range": 6,
    "nbr": 3,
    "nbr-on-same": 2
}


def getNearByRegion(loc, w, h):
    return Region(loc.x - w / 2, loc.y - h / 2, w, h)


def dist(pos1, pos2):
    return ((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2) ** 0.5


def squareDist(pos1, pos2):
    i = round(abs(pos1.x - pos2.x) / CELL_W)
    j = round(abs(pos1.y - pos2.y) / CELL_H)
    return max(int(i), int(j))


def similarColor(c1, c2, th=0.7):
    rmean = (c1.red + c2.red) / 2
    r = c1.red - c2.red
    g = c1.green - c2.green
    b = c1.blue - c2.blue
    return sqrt((((512 + rmean) * r * r) >> 8) + 4 * g * g + (((767 - rmean) * b * b) >> 8))


def getNearestCell(me_pos, tgt_pos, pm_nbr):
    if pm_nbr == 0:
        return None
    move_squares = getMoveSquares(me_pos, pm_nbr)
    dists_from_targets = list(map(lambda l: dist(tgt_pos, l), move_squares))
    tgts_dist = sorted(dists_from_targets)
    while tgts_dist:
        nearest_square_index = dists_from_targets.index(tgts_dist.pop(0))
        cell_pos = move_squares[nearest_square_index]
        getNearByRegion(cell_pos, 1, 1).highlight(0.1)
        if similarColor(cell_pos.getColor(), EMPTY_SQUARE_COLOR) < 50:
            return cell_pos
    return None


def getNearBy(loc, w, h):
    return Region(loc.getX() - w / 2, loc.getY() - h / 2, w, h)


def useRappelPotion():
    type(RAPPEL_POTION_SHORTCUT)
    wait(0.3)


def waitForChange(region):
    region.onChange(100)
    region.observe(10)
    region.stopObserver()


def waitVanish(region, time_out=20, scan_rate=0.8):
    snippet = Pattern(capture(region)).exact()
    time_elapsed = 0
    while time_elapsed < time_out:
        if not region.wait(snippet, 1 / scan_rate):
            return True
        time_elapsed += 1 / scan_rate
    return False


class ChangeObserver(threading.Thread):
    def __init__(self, region, scan_rate=3, sim=0.99):
        threading.Thread.__init__(self)
        self.region = region
        self.curr = Pattern(capture(self.region)).similar(sim)
        self.stopSignal = threading.Event()
        self.changed = threading.Event()
        self.scan_rate = scan_rate

    def stop(self):
        self.stopSignal.set()

    def run(self):
        while not self.stopSignal.is_set():
            if not self.region.wait(self.curr, 1 / self.scan_rate):
                self.changed.set()


class AppearObserver(threading.Thread):
    def __init__(self, region, pattern, callback, scan_rate=3, sim=0.99):
        threading.Thread.__init__(self)
        self.region = region
        self.callback = callback
        self.stopSignal = threading.Event()
        self.scan_rate = scan_rate
        self.pattern = pattern

    def stop(self):
        self.stopSignal.set()

    def run(self):
        while not self.stopSignal.is_set():
            if self.region.wait(self.pattern, 1 / self.scan_rate):
                self.callback()
                break




class Farmer(threading.Thread):

    def __init__(self, resource_pattern, src_path, nbr_cycles=1, start_step=0, max_pods=18000, min_pods=2000):
        threading.Thread.__init__(self, name='Farmer')
        self.stopSignal = threading.Event()
        self.resource_pattern = resource_pattern
        self.src_path = src_path
        self.curr_step = start_step
        self.nbr_cycles = nbr_cycles
        self.fighter_thread = Fighter(nbr_pm=5, spell=SOURNOISERIE, scan_rate=3)
        self.max_pods = 2071
        self.farm_path = self.loadFarmPath(self.src_path)
        self.curr_pods = min_pods

    def changeMap(self, tgt):
        log.info('changing map...')
        while not self.stopSignal.is_set():
            with lock:
                tgt.click()
            if waitVanish(MINIMAP_R):
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

                if self.fighter_thread.combatDetected.wait(0.5):
                    log.info('waiting for fighter to end...')
                    self.fighter_thread.combatEnded.wait()
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
                    resource_region = Region(*rec)
                    result.append((rtype, resource_region))
        return result


def cleanUp():
    fighter_thread.interrupt()
    # farmer_thread.interrupt()


if __name__ == "__main__":
    atexit.register(cleanUp)
    farming_path = "path01.txt"
    farm_path = os.path.join(SRC_DIR, farming_path)
    Settings.MoveMouseDelay = 0.3
    Settings.observeScanRate = 0.7
    # farmer_thread = Farmer(frifri.PATTERNS, farm_path, start_step=0, nbr_cycles=5)
    # farmer_thread.start()
    # farmer_thread.join()
    fighter_thread = Fighter(nbr_pm=5, spell=SOURNOISERIE, scan_rate=3)
    fighter_thread.start()
    fighter_thread.join()
