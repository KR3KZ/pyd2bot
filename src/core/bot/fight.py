import collections
import threading
from time import sleep, perf_counter
import pyautogui
from core import dofus
from core.bot import Walker
from core.exceptions import *
from core.grid import Grid
import logging

from network.message.msg import Msg
pyautogui.FAILSAFE = False

logger = logging.getLogger("bot")
class Fighter(Walker):

    def __init__(self, spell, workdir, name="Fighter"):
        super(Fighter, self).__init__(workdir, name)
        self.spell = spell
        self.grid = Grid(dofus.COMBAT_R, dofus.VCELLS, dofus.HCELLS)
        self.mobs_killed = 0
        self.nbr_fights = 0

    def run(self):
        super(Fighter, self).run()

    def onCombatEnded(self):
        self.combatEndReached.set()
        self.combatStarted.clear()
        pyautogui.press("escape")
        sleep(0.7)

    def handleMsg(self, msg: Msg):
        super().handleMsg(msg)
        if msg.msgType["name"] == "GameFightStartingMessage":
            """	
            {
                '__type__': 'GameFightStartingMessage',
                'attackerId': 290210840786.0,
                'containsBoss': False,
                'defenderId': -20008.0,
                'fightId': 2517,
                'fightType': 4}
            """
            msg_json = msg.json()
            self.id = msg_json["attackerId"]
            logger.info(msg_json)
            self.combatStarted.set()
        
        elif msg.msgType["name"] == "GameEntitiesDispositionMessage":
            """
            {
                '__type__': 'GameEntitiesDispositionMessage',
                'dispositions': [
                    {'__type__': 'IdentifiedEntityDispositionInformations',
                'cellId': 483,
                'direction': 7,
                'id': 290210840786.0}]
            }
            """
            msg_json = msg.json()
            cellId = msg_json["cellId"]
            x, y = dofus.getCellCoords(cellId)
            if msg_json["id"] == self.id:
                self.grid[x][y].type = dofus.ObjType.BOT
                self.grid.bot = self.grid[x][y]
            else:
                self.grid[x][y].type = dofus.ObjType.MOB
                self.grid.mobs.add(self.grid[x][y])
        
        elif msg.msgType["name"] == "GameFightShowFighterMessage":
            """{
                    '__type__': 'GameFightShowFighterMessage',
                    'informations': {'__type__': 'GameFightCharacterInformations',
                    'alignmentInfos': {'__type__': 'ActorAlignmentInformations',
                                     'alignmentGrade': 0,
                                     'alignmentSide': 0,
                                     'alignmentValue': 0,
                                     'characterPower': 290210840968.0},
                  'breed': 3,
                  'contextualId': 290210840786.0,
                  'disposition': {'__type__': 'FightEntityDispositionInformations',
                                  'carryingCharacterId': 0.0,
                                  'cellId': 483,
                                  'direction': 7},
                  'hiddenInPrefight': False,
                  'ladderPosition': 0,
                  'leagueId': 65535,
                  'level': 182,
                  'look': {'__type__': 'EntityLook',
                           'bonesId': 1,
                           'indexedColors': [32562098,
                                             35425736,
                                             52378184,
                                             68446613,
                                             89959123],
                           'scales': [120],
                           'skins': [30, 2046, 250, 1176, 75, 499],
                           'subentities': [{'__type__': 'SubEntity',
                                            'bindingPointCategory': 1,
                                            'bindingPointIndex': 0,
                                            'subEntityLook': {'__type__': 'EntityLook',
                                                              'bonesId': 264,
                                                              'indexedColors': [],
                                                              'scales': [80],
                                                              'skins': [],
                                                              'subentities': []}}]},
                  'name': 'John-shooter',
                  'previousPositions': [],
                  'sex': False,
                  'spawnInfo': {'__type__': 'GameContextBasicSpawnInformation',
                                'alive': True,
                                'informations': {'__type__': 'GameContextActorPositionInformations',
                                                 'contextualId': 290210840786.0,
                                                 'disposition': {'__type__': 'FightEntityDispositionInformations',
                                                                 'carryingCharacterId': 0.0,
                                                                 'cellId': 483,
                                                                 'direction': 7}},
                                'teamId': 0},
                  'stats': {'__type__': 'GameFightCharacteristics',
                            'characteristics': {'__type__': 'CharacterCharacteristics',
                                                'characteristics': [{'__type__': 'CharacterUsableCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 7,
                                                                     'characteristicId': 1,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 2,
                                                                     'used': 0},
                                                                    {'__type__': 'CharacterUsableCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 3,
                                                                     'characteristicId': 23,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 2,
                                                                     'used': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 37,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 3},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 33,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 65534},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 35,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 9},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 36,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 26},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 34,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 13,
                                                                     'characteristicId': 27,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 13,
                                                                     'characteristicId': 28,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 9},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 3,
                                                                     'characteristicId': 79,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 3,
                                                                     'characteristicId': 78,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 964,
                                                                     'characteristicId': 44,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 316},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 92,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 97,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 100,
                                                                     'characteristicId': 123,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 376,
                                                                     'characteristicId': 10,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 332},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 100,
                                                                     'characteristicId': 120,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 10},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 100,
                                                                     'characteristicId': 122,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 11,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 487},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 95,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 90,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 100,
                                                                     'characteristicId': 125,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 65524},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 14,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 30},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 65,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 13,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 60},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 88,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 91,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 960,
                                                                     'characteristicId': 0,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 100,
                                                                     'characteristicId': 107,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 25,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 15,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 76},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 25,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 12},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 16,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 19},
                                                                    {'__type__': 'CharacterCharacteristicDetailed',
                                                                     'additional': 0,
                                                                     'alignGiftBonus': 0,
                                                                     'base': 0,
                                                                     'characteristicId': 89,
                                                                     'contextModif': 0,
                                                                     'objectsAndMountBonus': 0}]},
                            'invisibilityState': 3,
                            'summoned': False,
                            'summoner': 0.0},
                  'status': {'__type__': 'PlayerStatus', 'statusId': 10},
                  'wave': 0}}"""
            pass
        
        elif msg.msgType["name"] == "GameFightEndMessage":
            """
            {'__type__': 'GameFightEndMessage',
                'duration': 9270,
                'lootShareLimitMalus': -1,
                'namedPartyTeamsOutcomes': [],
                'results': [{'__type__': 'FightResultPlayerListEntry',
                            'additional': [{'__type__': 'FightResultExperienceData',
                                            'experience': 1386623564,
                                            'experienceFightDelta': 37,
                                            'experienceForGuild': 0,
                                            'experienceForMount': 0,
                                            'experienceLevelFloor': 1355584000,
                                            'experienceNextLevelFloor': 1404179000,
                                            'isIncarnationExperience': False,
                                            'rerollExperienceMul': 1,
                                            'showExperience': True,
                                            'showExperienceFightDelta': True,
                                            'showExperienceForGuild': False,
                                            'showExperienceForMount': False,
                                            'showExperienceLevelFloor': True,
                                            'showExperienceNextLevelFloor': True}],
                            'alive': True,
                            'id': 290210840786.0,
                            'level': 182,
                            'outcome': 2,
                            'rewards': {'__type__': 'FightLoot',
                                        'kamas': 5,
                                        'objects': [287, 1, 6899, 1]},
                            'wave': 0},
                            {'__type__': 'FightResultFighterListEntry',
                            'alive': True,
                            'id': -1.0,
                            'outcome': 0,
                            'rewards': {'__type__': 'FightLoot', 'kamas': 0, 'objects': []},
                            'wave': 0}],
                'rewardRate': 0}
            """
            self.combatEnded.set()
            pass
    
    def onCombatStarted(self):
        self.grid.parse(self.currMapId)
        match = dofus.LVL_UP_INFO_R.find(dofus.CLOSE_POPUP_P)
        if match:
            match.click()
        try:
            logging.info("Combat started")
            self.combatStarted.set()
            self.combatEndReached.clear()
            self.combatEnded.clear()
            self.dead = False
            pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
            dofus.OUT_OF_COMBAT_R.hover()
            self.combatAlgo()
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
            if (1 / rate) - elapsed > 0:
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
                elif dofus.COMBAT_R.find(dofus.REDUCE_BOX_P):
                    dofus.COMBAT_R.find(dofus.REDUCE_BOX_P).click()
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
        while not self.combatEndReached.wait(1) and usedSpells < self.spell['nbr']:
            if not self.mobs_killed:
                self.mobs_killed = len(self.grid.mobs)
            if self.combatEndReached.wait(0.5):
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
                        if self.combatEndReached.wait(0.5):
                            return
                        self.useSpell(self.spell, mob)
                    else:
                        break
            else:
                self.useSpell(self.spell, mob)
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
    def useSpell(spell, target, timeout=2):
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

    def harvestCombats(self, mobs_patterns, max_tries=10, shuffle=False):
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

    def enterCombat(self, tgt, timeout=3.5):
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