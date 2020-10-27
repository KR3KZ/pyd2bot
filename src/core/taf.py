# from sikuli.Sikuli import QRect, Location, Pattern, capture, wait, FindFailed, Key, Settings
from sikuli.Sikuli import *
import threading
import atexit
from PyQt5.QtCore import QRect
import os
from math import sqrt
from src.core.log import Log


def getNearByRegion(loc, w, h):
    return QRect(loc.x - w / 2, loc.y - h / 2, w, h)


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
    return QRect(loc.getX() - w / 2, loc.getY() - h / 2, w, h)


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
