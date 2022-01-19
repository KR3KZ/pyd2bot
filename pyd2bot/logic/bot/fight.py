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
        self.isInFight = threading.Event()
        self.inFightTurn = threading.Event()
        self.canSayReady = threading.Event()
        self.isReady = threading.Event()
        self.spellAnimation = threading.Event()
        self.spellCasted = threading.Event()
        self.spellCast = None # {"spellId": , "cellID": }
        self.pa = None
        self.pm = None
        self.currCellId = None
        self.monsters = []

    def handleMsg(self, msg: Msg):
        super().handleMsg(msg)
        msg_json = msg.json()
        try:
            if msg.msgName == "GameFightStartingMessage":
                """	
                {
                    '__type__': 'GameFightStartingMessage',
                    'attackerId': 290210840786.0,
                    'containsBoss': False,
                    'defenderId': -20008.0,
                    'fightId': 2517,
                    'fightType': 4
                }
                """
                msg_json = msg.json()
                self.id = msg_json["attackerId"]
                self.isInFight.set()
            
            elif msg.msgName == "GameEntitiesDispositionMessage":
                """
                {
                    '__type__': 'GameEntitiesDispositionMessage',
                    'dispositions': [
                        {
                            '__type__': 'IdentifiedEntityDispositionInformations',
                            'cellId': 483,
                            'direction': 7,
                            'id': 290210840786.0
                        }
                    ]
                }
                """
                for disposition in msg_json["dispositions"]:
                    cellId = disposition["cellId"]
                    x, y = dofus.getCellCoords(cellId)
                    i, j = y, x//2
                    cell = self.grid[i][j]
                    logger.info(f"Element disposed in {(x, y)}")
                    if disposition["id"] == self.id:
                        cell.type = dofus.ObjType.BOT
                        self.grid.bot = cell
                    else:
                        cell.type = dofus.ObjType.MOB
                        self.grid.mobs.add(cell)
            
            elif msg.msgName == "GameFightShowFighterMessage":
                """
                {
                    '__type__': 'GameFightShowFighterMessage',
                    'informations': {
                        '__type__': 'GameFightCharacterInformations',
                        'breed': 3,
                        'contextualId': 290210840786.0,
                        'disposition': {
                            '__type__': 'FightEntityDispositionInformations',
                            'carryingCharacterId': 0.0,
                            'cellId': 483,
                            'direction': 7
                        },
                        'hiddenInPrefight': False,
                        'level': 182,
                        'name': 'John-shooter',
                        'previousPositions': [],
                        'sex': False,
                        'spawnInfo': {
                            '__type__': 'GameContextBasicSpawnInformation',
                            'alive': True,
                            'informations': {
                                '__type__': 'GameContextActorPositionInformations',
                                'contextualId': 290210840786.0,
                                'disposition': {
                                    '__type__': 'FightEntityDispositionInformations',
                                    'carryingCharacterId': 0.0,
                                    'cellId': 483,
                                    'direction': 7
                                }
                            }
                        },
                        'teamId': 0
                    },
                    'stats': {
                        '__type__': 'GameFightCharacteristics',
                        'invisibilityState': 3,
                        'summoned': False,
                        'summoner': 0.0
                    },
                    'status': {
                        '__type__': 'PlayerStatus', 
                        'statusId': 10
                    },
                    'wave': 0
                }
                """
                pass
            
            elif msg.msgName == "GameFightEndMessage":
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
                self.isInFight.clear()
            
            elif msg.msgName == "GameFightTurnStartPlayingMessage":
                logger.info("Bot turn started")
                self.inFightTurn.set()
            
            elif msg.msgName == "GameFightTurnFinishMessage":
                logger.info("Bot turn ended")
                self.inFightTurn.clear()
            
            elif msg.msgName == "GameFightJoinMessage":
                if msg_json["canSayReady"]:
                    logger.info("can say ready event set")
                    self.canSayReady.set()

            elif msg.msgName == "GameFightReadyMessage":
                if msg_json["isReady"]:
                    self.isReady.set()
            
            elif msg.msgName == "GameActionFightCastRequestMessage":
                logger.info("Spell casted")
                # if msg_json["cellId"] == self.spellCast["cellId"] and  msg_json["spellId"] == self.spellCast["spellId"] :
                #     self.spellCasted.set()
                        
            elif msg.msgName == "SequenceStartMessage":
                if msg_json["authorId"] == self.id and msg_json["sequenceType"] == 1:
                    self.spellAnimation.set()
                    
            elif msg.msgName == "SequenceEndMessage":
                if msg_json["authorId"] == self.id and msg_json["sequenceType"] == 1:
                    self.spellAnimation.clear()
                
            elif msg.msgName == "RefreshCharacterStatsMessage":
                if msg_json["fighterId"] == self.id:
                    for characteristic in msg_json["stats"]["characteristics"]["characteristics"]:
                        value = characteristic["additional"] + characteristic["alignGiftBonus"] + characteristic["base"] +\
                                characteristic["objectsAndMountBonus"]
                        if characteristic["characteristicId"] == 23:
                            self.pm = value - characteristic["used"]
                        elif characteristic["characteristicId"] == 1:
                            self.pa = value - characteristic["used"]
                    logger.info(f"Bot pa, pm: {self.pa, self.pm}")

            elif msg.msgName == "GameFightSynchronizeMessage":
                self.monsters = []
                for fighter in msg_json["fighters"]:
                    if fighter["__type__"] == "GameFightCharacterInformations" and fighter["contextualId"] == self.id:
                        self.currCellId = fighter["disposition"]["cellId"]
                        for characteristic in fighter["stats"]["characteristics"]["characteristics"]:
                            value = characteristic["additional"] + characteristic["alignGiftBonus"] + characteristic["base"] +\
                                characteristic["objectsAndMountBonus"]
                            if characteristic["characteristicId"] == 23:
                                self.pm = value - characteristic["used"]
                            elif characteristic["characteristicId"] == 1:
                                self.pa = value - characteristic["used"]
                    elif fighter["__type__"] == "GameFightMonsterInformations":
                        self.monsters.append(
                            {
                                "cellID": fighter["disposition"]["cellId"],
                                "summoned": fighter["stats"]["summoned"]
                            }
                        )
        except Exception:
            logger.error("Fatal error in msg handler!", exc_info=True)
            self.interrupt()
            
    def onCombatStarted(self):
        self.grid.parse(self.currMapId)
        try:
            logger.info(f"Combat started **** {self.canSayReady.is_set()}")
            if self.canSayReady.wait():
                for _ in range(6):
                    pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
                    logger.info("ready clicked")
                    if self.isReady.wait(0.2):
                        break
            while self.isInFight.is_set():sleep(0.1)
            logger.info("combat ended")
            # pyautogui.press(dofus.SKIP_TURN_SHORTCUT)
            # dofus.OUT_OF_COMBAT_R.hover()
            # self.combatAlgo()
        except Exception:
            logging.error("Fatal error in main run!", exc_info=True)
            self.interrupt()

    def interrupt(self):
        """
        interrupt thread.
        """
        dofus.READY_R.stopWait.set()
        self.isInFight.clear()
        super(Fighter, self).interrupt()

    def combatAlgo(self):
        self.mobs_killed = 0
        while not self.combatEnded.wait(1):
            self.checkCreatureMode()
            try:
                if not self.myTurn():
                    self.waitTurn()
                self.playTurn()
            except (FindPathFailed, MoveToCellFailed, UseSpellFailed, WaitTurnTimedOut) as e:
                if self.killsig.is_set():
                    return True
                if self.disconnected.is_set():
                    self.connected.wait()
                elif dofus.COMBAT_R.find(dofus.REDUCE_BOX_P):
                    dofus.COMBAT_R.find(dofus.REDUCE_BOX_P).click()
                else:
                    logging.error(str(e), exc_info=True)
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
        while usedSpells < self.spell['nbr']:
            if not self.mobs_killed:
                self.mobs_killed = len(self.grid.mobs)
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
        if self.isInFight.wait(timeout):
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