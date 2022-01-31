import collections
from time import sleep, perf_counter
from com.ankamagames.jerakine.types.positions.mapPoint import MapPoint
from .walker import Walker
from com.ankamagames.jerakine.logger.Logger import Logger
logger = Logger(__name__)

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
        try:
            logger.info(f"Combat started **** {self.canSayReady.is_set()}")
            if self.canSayReady.wait():
                self.sayReady()
                self.turnStarted.wait()
                self.combatAlgo()
            logger.info("combat ended")
        except Exception:
            logger.error("Fatal error in combat handle!", exc_info=True)
            self.stop()

    def combatAlgo(self):
        while self.isInFight.is_set():
            try:
                self.isTurn.wait()
                self.sayReady()
                self.turnStarted.wait()
                self.playTurn()
                self.endTurn()
                self.turnEnded.wait()
            except Exception as e:
                logger.error(str(e), exc_info=True)

    def sayReady(self):
        self.conn.send({
            '__type__': 'GameFightReadyMessage', 
            'isReady': True
        })

    def endTurn(self):
        self.conn.send({
            '__type__': 'GameFightTurnFinishMessage', 
            'isAfk': False
        })

    def playTurn(self):
        usedSpells = 0
        while usedSpells < self.spell['nbr']:
            target, path = self.findPathToTarget(self.spell['range'])
            if path:
                cell = self.cellToTarget(path)
                if cell:
                    self.moveToCell(cell)
                    if cell == path[-1]:
                        self.castSpell(self.spell, target)
                    else:
                        break
            else:
                self.castSpell(self.spell, target)
            usedSpells += 1

    @staticmethod
    def cellToTarget(path):
        if path[-1].reachable():
            return path[-1]
        for idx, cell in enumerate(path):
            if not cell.reachable():
                if idx == 0:
                    return None
                return path[idx - 1]
        return None

    def moveToCell(self, cell, timeout=10):
        # move to cell here
        pass

    def castSpell(spell, target, timeout=2):
        # use spell here
        pass
    
    def isMpReachable(self, mp):
        return self.currMap.cells[mp.cellId].isAccessibleDuringFight() and 
            # get map
        pass

    def findPathToTarget(self, startCellId, po, targets):
        logging.debug("searching path to mobs")
        refPosition = MapPoint.fromCellId(startCellId)
        queue = collections.deque([[refPosition]])
        seen = {refPosition}
        while not self._kill.is_set() and self.isInFight.is_set() and queue:
            path = queue.popleft()
            currMp = path[-1]
            for mobCellId in self.currMap.getMonsterEntitiesCellIds():
                spellRange = LosDetector.getRange(currMp, po)
                if mobCellId in LosDetector.getCell(self.currMap, spellRange, currMp):
                    return mobCellId, path[1:]
            for mp in self.getFightMpNeighbors(currMp):
                if mp not in seen and not self.currMap.hasEntity(mp.x, mp.y):
                    queue.append(path + [mp])
                    seen.add(mp)
        return None, None

    def getFightMpNeighbors(self, mp: MapPoint):
        neighbours = list[MapPoint]()
        for direction in range(8) :
            cell = self.currMap.getNeighbourCellFromDirection(mp.cellId, direction)
            if cell and cell.isAccessibleDuringFight():
                neighbours.append(MapPoint.fromCellId(cell.id))
        return neighbours

    def harvestCombats(self):
        # look for fight in map
        pass

    def enterCombat(self, tgt, timeout=3.5):
        # enter combat 
        pass