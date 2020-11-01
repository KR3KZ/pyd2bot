import collections
import threading
from time import sleep, perf_counter
import pyautogui
from core import dofus
from core.grid import Grid
from core.log import Log
import atexit
from core.observer import Observer
from core.cell import ParseFailed

log = Log()
lock = threading.Lock()

MAX_RETRIES = 5


def retry(fn):
    def wrapped(self, *args, **kwargs):
        for counter in range(MAX_RETRIES):
            try:
                result = fn(self, *args, **kwargs)
                break
            except (TimeoutError, ParseFailed) as e:
                if self.combatEnded.is_set():
                    return
                log.info(str(e))
                sleep(0.2)
                if counter == MAX_RETRIES - 1:
                    raise
        return result

    return wrapped


class Fighter(threading.Thread):
    def __init__(self, spell):
        threading.Thread.__init__(self, name='Fighter')
        self.spell = spell
        self.died = threading.Event()
        self.stopSignal = threading.Event()
        self.combatDetected = threading.Event()
        self.combatEnded = threading.Event()
        self.combatEndObs = None
        self.grid = Grid(dofus.COMBAT_R, dofus.VCELLS, dofus.HCELLS)
        self.targets = {}

    def run(self):
        log.info('Fighter running')
        while not self.stopSignal.wait(1):
            sleep(2)
            dofus.READY_R.waitAny([dofus.READY_BUTTON_P, dofus.SKIP_TURN_BUTTON_P])
            pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
            self.checkCreatureMode()
            self.combatDetected.set()
            self.combatEnded.clear()
            self.combatEndObs = Observer(dofus.COMBAT_ENDED_POPUP_R,
                                         dofus.COMBAT_ENDED_POPUP_P,
                                         self.onCombatEnded,
                                         Observer.Mode.APPEAR)
            self.combatEndObs.start()
            with lock:
                try:
                    self.combatAlgo()
                except Exception as e:
                    log.error(e, exc_info=True)
                    self.interrupt()
                    break
                self.combatDetected.clear()
                log.info('combat ended')
        log.info('Goodbye cruel world.')

    def waitTurn(self):
        while not self.stopSignal.wait(0.1) and not self.combatEnded.wait(0.1):
            if dofus.MY_TURN_CHECK_L.getpixel() == dofus.MY_TURN_C:
                log.info('Bot turn started')
                break

    def onCombatEnded(self):
        log.info("Fight ended detected")
        dofus.END_COMBAT_CLOSE_L.click()
        self.combatEnded.set()
        self.combatEndObs.stop()

    def interrupt(self):
        dofus.READY_R.stopWait.set()
        self.combatEnded.set()
        self.combatEndObs.stop()
        self.stopSignal.set()

    def combatAlgo(self):
        while not self.combatEnded.wait(1):
            self.waitTurn()
            usedSpells = 0
            try:
                while not self.combatEnded.wait(1) and usedSpells < self.spell['nbr']:
                    self.parseGrid()
                    mob, path = self.findPathToTarget(self.spell['range'])
                    if path:
                        tgt = self.getTarget(path)
                        if tgt:
                            self.moveTo(tgt)
                        if tgt == path[-1]:
                            self.useSpell(mob)
                        else:
                            break
                    else:
                        self.useSpell(mob)
                    usedSpells += 1
            except Exception as e:
                log.error(e, exc_info=True)
            pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
            sleep(1)

    @retry
    def parseGrid(self):
        self.grid.parse()
        if not self.grid.bot or not self.grid.mobs:
            self.grid.non_obstacle = set()
            raise ParseFailed("Enable to find bot or mobs pos!")

    def getTarget(self, path):
        if path[-1].reachable():
            return path[-1]
        for idx, cell in enumerate(path):
            if not cell.reachable():
                return path[idx - 1]
        return None

    @retry
    def moveTo(self, cell, timeout=1):
        start = perf_counter()
        cell.click()
        dofus.OUT_OF_COMBAT_R.hover()
        while perf_counter() - start < timeout:
            cell.parse(from_grid=False)
            if cell.occupiedWithBot():
                return True
        raise TimeoutError

    @retry
    def useSpell(self, target, timeout=1):
        pa_observer = Observer(dofus.PA_R, mode=Observer.Mode.CHANGE)
        pa_observer.start()
        pyautogui.press(self.spell['shortcut'])
        target.click()
        dofus.OUT_OF_COMBAT_R.hover()
        if not pa_observer.changed.wait(timeout):
            pa_observer.stop()
            raise TimeoutError
        pa_observer.stop()

    def findPathToTarget(self, po):
        queue = collections.deque([[self.grid.bot]])
        seen = {(self.grid.bot.i, self.grid.bot.j)}
        while queue:
            path = queue.popleft()
            curr = path[-1]
            for mob in self.grid.mobs:
                if curr.inLDV(mob, po):
                    return mob, path[1:]
            for cell in curr.neighbors():
                if (cell.i, cell.j) not in seen and not cell.occupied():
                    queue.append(path + [cell])
                    seen.add((cell.i, cell.j))
        raise Exception("Enable to find a valid path!")

    def checkCreatureMode(self):
        if dofus.CREATURE_MODE_R.find(dofus.CREATURE_MODE_OFF_P, grayscale=False):
            dofus.CREATURE_MODE_R.click()
            dofus.OUT_OF_COMBAT_R.hover()


def tearDown(fighter):
    fighter.interrupt()
    fighter.join()


if __name__ == "__main__":
    from core import env

    env.focusDofusWindow()
    fighter = Fighter(dofus.SOURNOISERIE)
    atexit.register(tearDown, fighter)
    fighter.start()
    fighter.join()
    env.focusIDEWindow()
