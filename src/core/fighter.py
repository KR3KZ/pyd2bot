import collections
import threading
from time import sleep, perf_counter
import pyautogui
from core import dofus
from core.exceptions import FindPathFailed, ParseCellFailed
from core.grid import Grid
from core.log import log
import atexit
from core.observer import Observer
from core.utils import retry


class Fighter(threading.Thread):
    def __init__(self, spell, parent=None):
        threading.Thread.__init__(self, name='Fighter')
        self.spell = spell
        self.died = threading.Event()
        self.killsig = threading.Event()
        self.combatDetected = threading.Event()
        self.stopRetry = threading.Event()
        self.combatEnded = threading.Event()
        self.combatEndedDetected = threading.Event()
        self.combatEndObs = None
        self.grid = Grid(dofus.COMBAT_R, dofus.VCELLS, dofus.HCELLS)
        self.parent = parent
        self.died = False
        if parent:
            self.lock = self.parent.lock
        else:
            self.lock = threading.Lock()
        self.nbr_fights = 0

    def run(self):
        try:
            log.info('Fighter running')
            while not self.killsig.wait(1):
                dofus.READY_R.waitAny([dofus.READY_BUTTON_P, dofus.SKIP_TURN_BUTTON_P])
                log.info("Combat started")
                if self.killsig.is_set():
                    return
                self.combatDetected.set()
                self.combatEndedDetected.clear()
                self.combatEnded.clear()
                self.stopRetry.clear()
                with self.lock:
                    self.died = False
                    pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
                    dofus.OUT_OF_COMBAT_R.hover()
                    self.checkCreatureMode()
                    self.combatEndObs = Observer(dofus.COMBAT_ENDED_POPUP_R,
                                                 dofus.COMBAT_ENDED_POPUP_P,
                                                 self.onCombatEnded,
                                                 Observer.Mode.APPEAR)
                    self.combatEndObs.start()
                    self.combatAlgo()
                    self.combatEnded.set()
                    self.combatDetected.clear()
                    self.nbr_fights += 1
                    log.info('Combat ended')
        except Exception as e:
            log.error(e, exc_info=True)
            if self.parent:
                self.parent.interrupt()
            else:
                self.interrupt()
        log.info('Goodbye cruel world.')

    def waitTurn(self):
        while not self.killsig.wait(0.25) and not self.combatEnded.wait(0.25):
            if dofus.MY_TURN_CHECK_L.getpixel() == dofus.MY_TURN_C:
                log.info('Bot turn started')
                break

    def onCombatEnded(self):
        log.info("Fight ended detected")
        dofus.END_COMBAT_CLOSE_L.click()
        dofus.COMBAT_ENDED_POPUP_R.waitVanish(dofus.COMBAT_ENDED_POPUP_P)
        self.combatEndedDetected.set()
        self.stopRetry.set()
        self.combatEndObs.stop()

    def interrupt(self):
        self.stopRetry.set()
        dofus.READY_R.stopWait.set()
        self.combatEnded.set()
        if self.combatEndObs:
            self.combatEndObs.stop()
        self.killsig.set()

    def combatAlgo(self):
        turns_skipped_on_error = 0
        while not self.combatEndedDetected.wait(1):
            self.waitTurn()
            usedSpells = 0
            try:
                while not self.combatEndedDetected.is_set() and usedSpells < self.spell['nbr']:
                    self.parseGrid(nbr_retries=200)
                    if self.combatEndedDetected.is_set():
                        return
                    try:
                        mob, path = self.findPathToTarget(self.spell['range'], self.grid.mobs)
                    except FindPathFailed:
                        mob, path = self.findPathToTarget(self.spell['range'], self.grid.invoke)
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
            except (ParseCellFailed, TimeoutError, FindPathFailed) as e:
                if self.combatEndedDetected.is_set():
                    return
                log.info("fatal error in main loop", exec_info=True)
                turns_skipped_on_error += 1
                if turns_skipped_on_error == 10:
                    self.died = True
                    self.resign()
                    return
            except KeyboardInterrupt:
                self.interrupt()
                return
            pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
            sleep(1)

    @retry
    def parseGrid(self):
        self.grid.parse()
        if not self.grid.bot or not self.grid.mobs:
            raise ParseCellFailed("Enable to find bot or mobs pos!")

    def getTarget(self, path):
        if path[-1].reachable():
            return path[-1]
        for idx, cell in enumerate(path):
            if not cell.reachable():
                if idx == 0:
                    return None
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
    def useSpell(self, target, timeout=3):
        pyautogui.press(self.spell['shortcut'])
        target.click()
        dofus.OUT_OF_COMBAT_R.hover()
        sleep(0.7)

    def findPathToTarget(self, po, targets):
        queue = collections.deque([[self.grid.bot]])
        seen = {(self.grid.bot.i, self.grid.bot.j)}
        while queue:
            path = queue.popleft()
            curr = path[-1]
            for mob in targets:
                if curr.inLDV(mob, po):
                    return mob, path[1:]
            for cell in curr.neighbors():
                if (cell.i, cell.j) not in seen and not cell.occupied():
                    queue.append(path + [cell])
                    seen.add((cell.i, cell.j))
        raise FindPathFailed("Enable to find a valid path!")

    def checkCreatureMode(self):
        if dofus.CREATURE_MODE_R.find(dofus.CREATURE_MODE_OFF_P, grayscale=False):
            dofus.CREATURE_MODE_R.click()
            dofus.OUT_OF_COMBAT_R.hover()

    def resign(self):
        dofus.RESIGN_BUTTON_LOC.click()
        dofus.RESGIN_POPUP_R.waitAppear(dofus.RESIGN_POPUP_P)
        dofus.RESIGN_CONFIRM_L.click()
        dofus.RESGIN_POPUP_R.waitVanish(dofus.RESIGN_POPUP_P)
        dofus.DEFEAT_POPUP_R.waitAppear(dofus.DEFEAT_POPUP_P)
        dofus.DEFEAT_POPUP_CLOSE_L.click()
        dofus.DEFEAT_POPUP_R.waitVanish(dofus.DEFEAT_POPUP_P)


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
