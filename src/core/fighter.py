import collections
import threading
from time import sleep, perf_counter
import pyautogui
from core import dofus
from core.exceptions import FindPathFailed, ParseCellFailed
from core.grid import Grid
import logging
import atexit
from core.observer import Observer
from core.utils import retry


pyautogui.FAILSAFE = False


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
        self.mobs_killed = 0
        if parent:
            self.lock = self.parent.lock
        else:
            self.lock = threading.Lock()
        self.nbr_fights = 0

    def run(self):
        try:
            logging.debug('Fighter running')
            while not self.killsig.wait(1):
                dofus.READY_R.waitAny([dofus.READY_BUTTON_P, dofus.SKIP_TURN_BUTTON_P])
                logging.debug("Combat started")
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
                    logging.debug('Combat ended')
        except Exception as e:
            logging.error(e, exc_info=True)
            if self.parent:
                self.parent.interrupt()
            else:
                self.interrupt()
        logging.debug(f"I farmed {self.nbr_fights} fights")
        logging.debug('Goodbye cruel world.')

    def waitTurn(self):
        while not self.killsig.wait(0.25) and \
                not self.combatEnded.wait(0.25):
            if dofus.MY_TURN_CHECK_L.getpixel() == dofus.MY_TURN_C:
                logging.debug('Bot turn started')
                break

    def onCombatEnded(self):
        logging.debug("Fight ended detected")
        self.combatEndedDetected.set()
        self.stopRetry.set()
        self.combatEndObs.stop()
        dofus.END_COMBAT_CLOSE_L.click()
        dofus.COMBAT_ENDED_POPUP_R.waitVanish(dofus.COMBAT_ENDED_POPUP_P)

    def interrupt(self):
        self.stopRetry.set()
        dofus.READY_R.stopWait.set()
        self.combatEnded.set()
        if self.combatEndObs:
            self.combatEndObs.stop()
        self.killsig.set()

    def combatAlgo(self):
        turns_skipped_on_error = 0
        self.mobs_killed = 0
        while not self.combatEndedDetected.wait(1):
            self.waitTurn()
            usedSpells = 0
            try:
                while not self.combatEndedDetected.wait(0.2) and usedSpells < self.spell['nbr']:
                    self.parseGrid(nbr_retries=200)
                    logging.debug("combat grid parsed successfully")
                    logging.debug(f"fighting {len(self.grid.mobs)} mobs")
                    if not self.mobs_killed:
                        self.mobs_killed = len(self.grid.mobs)
                    if self.combatEndedDetected.is_set():
                        return
                    try:
                        logging.debug("searching path to mobs")
                        mob, path = self.findPathToTarget(self.grid.bot, self.spell['range'], self.grid.mobs)
                    except FindPathFailed:
                        mob, path = self.findPathToTarget(self.grid.bot, self.spell['range'], self.grid.invoke)
                    if path:
                        logging.debug("path found")
                        tgt = self.getTarget(path)
                        if tgt:
                            logging.debug("moving towards target")
                            self.moveTo(tgt)
                        if tgt == path[-1]:
                            logging.debug("can hit target")
                            self.useSpell(self.spell, mob)
                        else:
                            break
                    else:
                        self.useSpell(self.spell, mob)
                    usedSpells += 1
            except (ParseCellFailed, TimeoutError, FindPathFailed) as e:
                if self.combatEndedDetected.is_set():
                    return
                logging.info(str(e))
                turns_skipped_on_error += 1
                if turns_skipped_on_error == 10:
                    self.died = True
                    self.resign()
                    return
            except KeyboardInterrupt:
                self.interrupt()
                return
            pyautogui.press(dofus.SKIP_TURN_SHORTCUT)

    @retry
    def parseGrid(self):
        self.grid.parse()
        if not self.grid.bot or not self.grid.mobs:
            raise ParseCellFailed("Enable to find bot or mobs pos!")

    @staticmethod
    def getTarget(path):
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
    def useSpell(self, spell, target):
        pyautogui.press(spell['shortcut'])
        target.click()
        dofus.OUT_OF_COMBAT_R.hover()
        sleep(0.7)

    def findPathToTarget(self, start_cell, po, targets):
        queue = collections.deque([[start_cell]])
        seen = {start_cell.indexes()}
        while queue and not self.combatEndedDetected.is_set():
            path = queue.popleft()
            curr = path[-1]
            for mob in targets:
                if curr.inLDV(mob, po):
                    return mob, path[1:]
            for cell in curr.neighbors():
                if (cell.i, cell.j) not in seen and not cell.occupied():
                    queue.append(path + [cell])
                    seen.add(cell.indexes())
        raise FindPathFailed("Enable to find a valid path!")

    @staticmethod
    def checkCreatureMode():
        if dofus.CREATURE_MODE_R.find(dofus.CREATURE_MODE_OFF_P, grayscale=False):
            dofus.CREATURE_MODE_R.click()
            dofus.OUT_OF_COMBAT_R.hover()

    @staticmethod
    def resign():
        dofus.RESIGN_BUTTON_LOC.click()
        dofus.RESIGN_POPUP_R.waitAppear(dofus.RESIGN_POPUP_P)
        dofus.RESIGN_CONFIRM_L.click()
        dofus.RESIGN_POPUP_R.waitVanish(dofus.RESIGN_POPUP_P)
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
