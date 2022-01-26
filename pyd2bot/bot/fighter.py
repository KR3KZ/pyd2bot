import collections
from time import sleep, perf_counter
from .walker import Walker
import logging

logger = logging.getLogger("bot")

class Fighter(Walker):

    def __init__(self, spell, workdir, name="Fighter"):
        super(Fighter, self).__init__(workdir, name)
        self.spell = spell
        self.mobs_killed = 0
        self.spellCast = None # {"spellId": , "cellID": }
        self.pa = None
        self.pm = None
        self.currCellId = None
        self.monsters = []
            
    def onCombatStarted(self):
        self.grid.parse(self.currMapId)
        try:
            logger.info(f"Combat started **** {self.canSayReady.is_set()}")
            if self.canSayReady.wait():
                for _ in range(6):
                    # skip turn here
                    logger.info("ready clicked")
                    if self.isReady.wait(0.2):
                        break
            while self.isInFight.is_set():sleep(0.1)
            logger.info("combat ended")
        except Exception:
            logging.error("Fatal error in main run!", exc_info=True)
            self.interrupt()

    def combatAlgo(self):
        self.mobs_killed = 0
        while not self.combatEnded.wait(1):
            try:
                self.waitTurn()
                self.playTurn()
                self.skipTurn()
            except Exception as e:
                logging.error(str(e), exc_info=True)

    def skipTurn(self):
        # skip turn msg send here
        pass

    def waitTurn(self):
        # wait bort turn msg here 
        pass

    def playTurn(self):
        usedSpells = 0
        while usedSpells < self.spell['nbr']:
            target, path = self.findPathToTarget(self.spell['range'])
            if path:
                cell = self.cellToTarget(path)
                if cell:
                    self.moveToCell(cell)
                    if cell == path[-1]:
                        self.useSpell(self.spell, target)
                    else:
                        break
            else:
                self.useSpell(self.spell, target)
            usedSpells += 1

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
        # move to cell here
        pass

    @staticmethod
    def useSpell(spell, target, timeout=2):
        """
        Cast given spell on the target
        :param spell: spell dictionary
        :param target: targeted cell
        :param timeout: time out in seconds
        :return: True if all good else raise UseSpellFailed
        """
        # use spell here
        pass

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


    def harvestCombats(self, mobs_patterns, max_tries=10, shuffle=False):
        """
        Look for mobs patterns and try to enter combats.
        :param mobs_patterns: list of images
        :param max_tries: max number of clicks on mobs group
        :param shuffle: if you want to shuffle mobs patterns before matching
        :return: nbr of mobs farmed and the matched patterns with nbr of times matched
        """
        # look for fight in map
        pass

    def enterCombat(self, tgt, timeout=3.5):
        """
        Click on a mob group and wait for the combat to start.
        :param tgt: pos of mobs group in the screen
        :param timeout: timeout in seconds
        :return: True if all good else False
        """
        # enter combat 
        pass