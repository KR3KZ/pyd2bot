import collections
import threading
from time import sleep, perf_counter
import pyautogui
from core import dofus
from core.bot import Walker
from core.exceptions import *
from core.grid import Grid
import logging
pyautogui.FAILSAFE = False


class CombatStartObs(threading.Thread):
    def __init__(self, bot, rate=3):
        super(CombatStartObs, self).__init__()
        self.bot = bot
        self.rate = rate

    def run(self):
        while not self.bot.killsig.wait(1):
            patterns = [dofus.READY_BUTTON_P, dofus.SKIP_TURN_BUTTON_P]
            match, idx = dofus.READY_R.waitAny(patterns)
            self.bot.onCombatStarted('combat' if idx == 0 else 'turn')
            self.bot.combatEnded.wait()


class CombatEndObs(threading.Thread):
    def __init__(self, bot, rate=3):
        super(CombatEndObs, self).__init__()
        self.bot = bot
        self.rate = rate

    def run(self):
        while not self.bot.killsig.is_set():
            if self.bot.combatStarted.wait(1 / self.rate) and \
                    dofus.COMBAT_ENDED_POPUP_R.waitAppear(dofus.COMBAT_ENDED_POPUP_P, rate=self.rate):
                self.bot.onCombatEnded()


class Fighter(Walker):

    def __init__(self, spell, name="Fighter"):
        super(Fighter, self).__init__(name)
        self.spell = spell
        self.fightEndObs = CombatEndObs(self)
        self.fightStartObs = CombatStartObs(self)
        self.grid = Grid(dofus.COMBAT_R, dofus.VCELLS, dofus.HCELLS)
        self.mobs_killed = 0
        self.nbr_fights = 0

    def run(self):
        super(Fighter, self).run()
        self.fightStartObs.start()
        self.fightEndObs.start()

    def onCombatEnded(self):
        self.combatEndReached.set()
        self.combatStarted.clear()
        dofus.COMBAT_ENDED_POPUP_CLOSE_R.click()
        dofus.COMBAT_ENDED_POPUP_R.waitAnimationEnd()

    def onCombatStarted(self, event):
        try:
            logging.info("Combat started")
            self.combatStarted.set()
            self.combatEndReached.clear()
            self.combatEnded.clear()
            self.dead = False
            if event == 'combat':
                pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
            dofus.OUT_OF_COMBAT_R.hover()
            self.combatAlgo()
            self.combatEnded.set()
            self.nbr_fights += 1
            logging.debug('Combat ended')
        except Exception:
            logging.error("Fatal error in main run!", exc_info=True)
            self.interrupt()
        logging.info(f"I farmed {self.nbr_fights} fights")
        logging.info('Goodbye cruel world.')

    def waitTurn(self, rate=3, timeout=60 * 2):
        """
        Waits for bot turn.
        :param timeout: timeout in seconds
        :param rate: scan rate
        """
        s = perf_counter()
        while not self.killsig.is_set() and\
                not self.combatEndReached.is_set() and\
                perf_counter() - s < timeout:
            s = perf_counter()
            if self.myTurn():
                logging.debug('Bot turn started')
                return True
            elapsed = perf_counter() - s
            sleep((1 / rate) - elapsed)
        raise WaitTurnTimedOut

    def interrupt(self):
        """
        interrupt thread.
        """
        dofus.READY_R.stopWait.set()
        self.combatEnded.set()
        super(Fighter, self).interrupt()

    def combatAlgo(self):
        nbr_errors = 0
        self.mobs_killed = 0
        while not self.combatEndReached.wait(1):
            self.checkCreatureMode()
            try:
                if not self.myTurn():
                    self.waitTurn()
                self.playTurn()
                nbr_errors = 0
            except (FindPathFailed, ParseGridFailed, MoveToCellFailed, UseSpellFailed, WaitTurnTimedOut) as e:
                if self.combatEndReached.is_set() or self.killsig.is_set():
                    return True
                if self.disconnected.is_set():
                    self.connected.wait()
                else:
                    logging.error(str(e), exc_info=True)
                    nbr_errors += 1
                    logging.debug(f"Will skip bots turn for the '{nbr_errors}'th time!")
                    if nbr_errors == 10:
                        logging.debug("Reached maximum of turns skip on error. Will resign combat.")
                        self.dead = True
                        self.resign()
                        return False
            self.skipTurn()

    @staticmethod
    def skipTurn():
        pyautogui.press(dofus.SKIP_TURN_SHORTCUT)

    @staticmethod
    def myTurn():
        return dofus.MY_TURN_CHECK_L.getpixel() == dofus.MY_TURN_C

    def playTurn(self):
        """
        Play turn loop
        """
        usedSpells = 0
        while not self.combatEndReached.wait(0.2) and usedSpells < self.spell['nbr']:
            self.parseCombatGrid()
            if not self.mobs_killed:
                self.mobs_killed = len(self.grid.mobs)
            if self.combatEndReached.is_set():
                return
            mob, path = self.findPathToTarget(self.grid.bot, self.spell['range'], self.grid.mobs)
            if not mob:
                mob, path = self.findPathToTarget(self.grid.bot, self.spell['range'], self.grid.invoke)
            if not mob:
                raise FindPathFailed(self.grid)
            if path:
                cell = self.cellToTarget(path)
                if cell:
                    self.moveToCell(cell)
                    if cell == path[-1]:
                        self.useSpell(self.spell, mob)
                    else:
                        break
            else:
                self.useSpell(self.spell, mob)
            usedSpells += 1

    def parseCombatGrid(self, timeout=5):
        """
        Parse combat grid.
        :param timeout:  time out in seconds
        :return: True if all good else raise ParseGridFailed
        """
        s = perf_counter()
        while not self.killsig.is_set() and\
                not self.combatEndReached.is_set() and\
                perf_counter() - s < timeout:
            if self.grid.parse():
                return True
        raise ParseGridFailed(self.grid)

    @staticmethod
    def cellToTarget(path):
        """
        Get nearest reachable cell to target
        :param path: path to targeted cell
        :return: Reachable cell if any else None
        """
        if path[-1].reachable():
            return path[-1]
        for idx, cell in enumerate(path):
            if not cell.reachable():
                if idx == 0:
                    return None
                return path[idx - 1]
        return None

    def moveToCell(self, cell, timeout=10):
        """
        Move to a target cell.
        :param cell: cell object
        :param timeout: time out in seconds
        :return: True if all good else raise MoveToCellFailed
        """
        s = perf_counter()
        while not self.killsig.is_set() and \
                not self.combatEndReached.is_set() and \
                perf_counter() - s < timeout:
            cell.click()
            dofus.OUT_OF_COMBAT_R.hover()
            if cell.waitAppear(dofus.ObjType.BOT, 1):
                return True
        raise MoveToCellFailed(cell)

    @staticmethod
    def useSpell(spell, target, timeout=10):
        """
        Cast given spell on the target
        :param spell: spell dictionary
        :param target: targeted cell
        :param timeout: time out in seconds
        :return: True if all good else raise UseSpellFailed
        """
        pyautogui.press(spell['shortcut'])
        target.click()
        dofus.OUT_OF_COMBAT_R.hover()
        if target.waitAnimation(timeout):
            sleep(0.2)
            return True

        raise UseSpellFailed(target)

    def findPathToTarget(self, start_cell, po, targets):
        """
        Find path to the closest ldv to hit a mob.
        :param start_cell: position of the character
        :param po: range of the ldv
        :param targets: positions of the mobs
        :return: cell of the mob, path to the ldv if any else None
        """
        logging.debug("searching path to mobs")
        queue = collections.deque([[start_cell]])
        seen = {start_cell.indexes()}
        while not self.killsig.is_set() and not self.combatEndReached.is_set() and queue:
            path = queue.popleft()
            curr = path[-1]
            for mob in targets:
                if curr.inLDV(mob, po):
                    return mob, path[1:]
            for cell in curr.neighbors():
                if (cell.i, cell.j) not in seen and not cell.occupied():
                    queue.append(path + [cell])
                    seen.add(cell.indexes())
        return None, None

    @staticmethod
    def checkCreatureMode():
        """
        Check creature mode at the start of the fight if its not checked.
        """
        if dofus.CREATURE_MODE_R.find(dofus.CREATURE_MODE_OFF_P, grayscale=False):
            dofus.CREATURE_MODE_R.click()
            dofus.OUT_OF_COMBAT_R.hover()

    def harvestCombats(self, mobs_patterns, max_tries=4, shuffle=False):
        """
        Look for mobs patterns and try to enter combats.
        :param mobs_patterns: list of images
        :param max_tries: max number of clicks on mobs group
        :param shuffle: if you want to shuffle mobs patterns before matching
        :return: nbr of mobs farmed and the matched patterns with nbr of times matched
        """
        nbr_fails = 0
        result = {
            "farmed": 0,
            "matched": {}
        }
        while not self.killsig.is_set() and nbr_fails < max_tries:
            logging.debug("Searching for mobs group...")
            tgt, idx = dofus.COMBAT_R.findAny(mobs_patterns, threshold=0.8, shuffle=shuffle)
            if tgt:
                logging.debug("I found a mob group")
                if self.enterCombat(tgt):
                    nbr_fails = 0
                    if idx not in result['matched']:
                        result['matched'][idx] = 0
                    result['matched'][idx] += 1
                    self.combatEnded.wait()
                    result["farmed"] += self.mobs_killed
                    if self.dead:
                        logging.debug("Walker dead during combat!")
                        break
                else:
                    nbr_fails += 1
            else:
                logging.debug("No mobs found")
                break
        return result

    def enterCombat(self, tgt, timeout=5):
        """
        Click on a mob group and wait for the combat to start.
        :param tgt: pos of mobs group in the screen
        :param timeout: timeout in seconds
        :return: True if all good else False
        """
        tgt.click()
        logging.debug("Clicked on mobs group")
        s = perf_counter()
        if self.combatStarted.wait(timeout):
            logging.debug(f"Enter combat took: {perf_counter() - s}")
            return True
        logging.debug("Couldn't open combat!")
        return False

    @staticmethod
    def resign():
        """
        Abandon combat.
        """
        dofus.RESIGN_BUTTON_LOC.click()
        dofus.RESIGN_POPUP_R.waitAppear(dofus.RESIGN_POPUP_P)
        dofus.RESIGN_CONFIRM_L.click()
        dofus.RESIGN_POPUP_R.waitVanish(dofus.RESIGN_POPUP_P)
        dofus.DEFEAT_POPUP_R.waitAppear(dofus.DEFEAT_POPUP_P)
        dofus.DEFEAT_POPUP_CLOSE_L.click()
        dofus.DEFEAT_POPUP_R.waitVanish(dofus.DEFEAT_POPUP_P)