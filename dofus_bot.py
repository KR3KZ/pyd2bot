# from sikuli.Sikuli import Region, Location, Pattern, capture, wait, FindFailed, Key, Settings
from sikuli.Sikuli import *
import java.awt.Color as Color
import threading
import atexit
from math import sqrt
import traceback
import frighost_fish as frifri
import logging
import os
from time import sleep

lock = threading.Lock()

SRC_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
def get_log():
    format = "<%(asctime)-15s %(levelname)s line %(lineno)d %(threadName)s> %(funcName)s: - %(message)s"
    log_path = os.path.join(SRC_DIR, "bot.log")
    logging.basicConfig(filename=log_path, level=logging.INFO, format=format)
    return logging.getLogger("bot logger")
# bot log 
log = get_log()

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
READY_BUTTON_P = Pattern("1603357824947.png")
COMBAT_ENDED_POPUP_P = "END_COMBAT_P.png"
SKIP_TURN_BUTTON_P = "YOUR_TURN_P.png"
BOT_P = [Pattern("ME_P1.png").targetOffset(3, 3), Pattern("ME_P2.png").similar(0.65).targetOffset(-3, 8),
         Pattern("1603394186463.png").similar(0.68).targetOffset(2, 2),
         Pattern("1603394202485.png").targetOffset(-2, -8),
         Pattern("1603403880774.png").similar(0.61).targetOffset(1, 13), Pattern("1603408051708.png").targetOffset(5, 7),
         Pattern("1603408090329.png").targetOffset(0, -6),
         Pattern("1603424428505.png").similar(0.67).targetOffset(2, 15),
         Pattern("1603429082703.png").targetOffset(-2, -1), Pattern("rl.png").similar(0.67).targetOffset(-3, 16)]
MOB_P = [Pattern("1603396008837.png").targetOffset(-1, 9),
         Pattern("1603396021085.png").similar(0.50).targetOffset(-1, 8), Pattern("mobDown001.png").targetOffset(7, 1),
         Pattern("1603396075836.png").targetOffset(-2, 6), Pattern("mobDown002.png").targetOffset(3, 3),
         Pattern("mobleft001.png").targetOffset(0, -2), Pattern("mobleft002.png").similar(0.65).targetOffset(-11, 6),
         Pattern("mobLeft003.png").targetOffset(1, -4), Pattern("mobRight001.png").targetOffset(-3, 3),
         Pattern("1603457672046.png").targetOffset(9, 12)]

# Env Vars
NBR_H_CELL = 14.5
NBR_V_CELL = 20.5
EMPTY_SQUARE_COLOR = Color(90, 125, 62)
MY_TURN_COLOR = Color(252, 200, 0)
DU = (-1, -1)
DL = (-1, 1)
DD = (1, 1)
DR = (1, -1)

# Locations
MY_TURN_CHECK_LOC = Location(1431, 965)
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


def highlightPath(start_loc, path):
    x = start_loc.x
    y = start_loc.y
    for dx, dy in path:
        x = x + dx * CELL_W
        y = y + dy * CELL_H
        Region(x, y, 1, 1).highlight(0.2)
    return Location(x, y)


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


def getMoveSquares(loc, pm):
    V = []
    if pm != 0:
        from itertools import product
        for i, j in product(range(-pm, pm + 1), range(-pm, pm + 1)):
            if (i != 0 or j != 0) and (i + j) % 2 == 0 and max(abs(i), abs(j)) <= pm:
                square_pos = Location(loc.x + i * CELL_W, loc.y + j * CELL_H)
                if similarColor(square_pos.getColor(), EMPTY_SQUARE_COLOR) < 100:
                    # log.info(similarColor(square_pos.getColor(), EMPTY_SQUARE_COLOR))
                    V.append(square_pos)
    return V


def mobExists(mobs, mob):
    for m in mobs:
        if squareDist(m.getTarget(), mob.getTarget()) == 0:
            return True
    return False


def removeDuplicates(mobs):
    res = []
    for mob in mobs:
        if not mobExists(res, mob):
            res.append(mob)
    return res


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


class Fighter(threading.Thread):
    def __init__(self, nbr_pm, spell, scan_rate=3):
        threading.Thread.__init__(self, name='Farmer')
        self.scan_rate = scan_rate
        self.spell = spell
        self.nbr_pm = nbr_pm
        self.died = threading.Event()
        self.stopSignal = threading.Event()
        self.combatDetected = threading.Event()
        self.combatEnded = threading.Event()
        self.combat_ended_observer = AppearObserver(COMBAT_ENDED_POPUP_R, COMBAT_ENDED_POPUP_P, self.onCombatEnded)

    def run(self):
        log.info('fighter running')
        while not self.stopSignal.is_set():
            self.waitCombatStarted()
            if self.stopSignal.is_set():
                break
            with lock:
                wait(0.5)
                READY_R.click()
                try:
                    self.combatAlgo()
                except Exception as e:
                    log.info(traceback.print_exc())
                    self.interrupt()
                self.combatDetected.clear()
                log.info('combat ended')
        log.info('fighter stopped')

    def waitCombatStarted(self):
        while not self.stopSignal.is_set():
            try:
                READY_R.wait(READY_BUTTON_P, 1. / self.scan_rate)
                self.combatDetected.set()
                log.info('Combat started')
                break
            except FindFailed as e:
                pass

    def interrupt(self):
        self.combat_ended_observer.stop()
        self.combat_ended_observer.join()
        self.combatEnded.set()
        self.stopSignal.set()

    def waitTurn(self):
        while not self.stopSignal.is_set() and not self.combatEnded.is_set():
            if MY_TURN_CHECK_R.getTarget().getColor() == MY_TURN_COLOR:
                log.info('Bot turn started')
                break
            wait(0.33)

    def onCombatEnded(self):
        log.info("combat ended detected")
        END_COMBAT_CLOSE_L.click()
        wait(0.2)
        self.combat_ended_observer.stop()
        self.combat_ended_observer.join()
        self.combatEnded.set()

    @staticmethod
    def findMapPatterns():
        bot = COMBAT_R.findBest(BOT_P)
        if not bot:
            raise Exception("Enable to find bot position")
        mobs = []
        for patt in MOB_P:
            try:
                mobs += COMBAT_R.findAll(patt)
            except FindFailed as e:
                pass
        mobs = removeDuplicates(mobs)
        if not mobs:
            raise Exception("Couldn't detect mobs positions")
        return bot, mobs

    @staticmethod
    def selectTarget(mobs, bot):
        idx = min(range(len(mobs)), key=lambda it: squareDist(mobs[it].getTarget(), bot.getTarget()))
        match = mobs[idx]
        pos = match.getTarget()
        tgt = {'idx': idx,
               'match': match,
               'pos': pos,
               'color': pos.getColor(),
               'dist': squareDist(pos, bot.getTarget()),
               'r': Region(match),
               'snippet': Pattern(capture(Region(match))),
               'nbr-casted-on': 0,
               'in-range': False
               }
        return tgt

    def useSpell(self, target):
        pa_observer = ChangeObserver(PA_R)
        pa_observer.start()
        type(self.spell['shortcut'])
        target.click()
        res = pa_observer.changed.wait(3)
        pa_observer.join()
        return res

    def combatAlgo(self):
        log.info('combat started')
        self.combatEnded.clear()
        self.combat_ended_observer.start()

        # main combat loop
        while not self.combatEnded.wait(1):
            self.waitTurn()

            # Detect mobs and bot positions and highlight them
            bot, mobs = self.findMapPatterns()
            bot_pos = bot.getTarget()
            log.info("detected :{}, mobs".format(len(mobs)))
            for m in mobs:
                Region(m).highlight(0.1)
            Region(bot).highlight(0.1)

            # select nearest target to hit
            target = self.selectTarget(mobs, bot)
            spell_nbr = self.spell['nbr']
            pm = self.nbr_pm

            # in turn loop
            while not self.stopSignal.is_set() and spell_nbr > 0:
                log.info('My distance from target = ' + str(target['dist']))
                log.info("pm: ", pm, ", nbr spell: ", spell_nbr)

                # if target is in spell range
                if target['dist'] <= self.spell['range']:
                    log.info("target is in spell range")
                    target['in-range'] = True

                    # if nbr casts allowed reached try to switch target
                    if target['nbr-casted-on'] == self.spell['nbr-on-same']:
                        if len(mobs) > 1:
                            other_mobs = [m for m in mobs if m != target['match']]
                            target = self.selectTarget(other_mobs, bot)
                        else:
                            # cant recast the spell on target and no other targets
                            break

                    # if spell hits the target
                    if self.useSpell(target['pos']):
                        log.info("I touched the target")
                        spell_nbr -= 1
                        target['nbr-casted-on'] += 1
                        # if target dies after spell cast
                        if not target['r'].wait(target['snippet'], 3):
                            log.info("target died")
                            if len(mobs) == 1:
                                self.combatEnded.wait(5)
                                return
                            else:
                                mobs.pop(target['idx'])
                                target = self.selectTarget(mobs, bot)
                        continue

                log.info("I can't hit the target")
                # if target not reachable and bot has not pms skip turn
                if pm == 0:
                    break

                if self.stopSignal.is_set(): return
                if target['in-range']:
                    search_range = pm
                else:
                    search_range = min(pm, target['dist'] - self.spell['range'])

                cell_pos = getNearestCell(bot_pos, target['pos'], search_range)

                if cell_pos:
                    pm_to_cell = squareDist(cell_pos, bot_pos)
                    log.info("moving {} to new nearest cell".format(pm_to_cell))
                    cell_pos.click()
                    pm = pm - pm_to_cell
                    bot_pos = cell_pos
                    target['dist'] = squareDist(target['pos'], bot_pos)

            # skip turn
            OUT_OF_COMBAT_R.hover()
            log.info("bot skipped his turn")
            type(Key.SPACE)
            wait(0.5)


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
    farming_path = "frighost_fish.sikuli\\path01.txt"
    farm_path = os.path.join(SRC_DIR, farming_path)
    Settings.MoveMouseDelay = 0.3
    Settings.observeScanRate = 0.7
    # farmer_thread = Farmer(frifri.PATTERNS, farm_path, start_step=0, nbr_cycles=5)
    # farmer_thread.start()
    # farmer_thread.join()
    fighter_thread = Fighter(nbr_pm=5, spell=SOURNOISERIE, scan_rate=3)
    fighter_thread.start()
    fighter_thread.join()
