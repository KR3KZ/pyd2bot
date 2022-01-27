import logging
from pyd2bot.game.fight.types.FighterStatus import FighterStatus
logger = logging.getLogger("bot")


_entityStates = dict()
   
   
def addStateOnTarget(targetId:float, stateId:int, delta:int = 1) -> None:
   if not _entityStates[targetId]:
      _entityStates[targetId] = dict()

   if not _entityStates[targetId][stateId]:
      _entityStates[targetId][stateId] = delta

   else:
      _entityStates[targetId][stateId] += delta
      
def removeStateOnTarget(targetId:float, stateId:int, delta:int = 1) -> None:
   if not _entityStates[targetId]:
      logger.error("Can\'t find state list for " + targetId + " to remove state")
      return

   if _entityStates[targetId][stateId]:
      _entityStates[targetId][stateId] -= delta
      if _entityStates[targetId][stateId] == 0:
         del _entityStates[targetId][stateId]

def hasState(targetId:float, stateId:int) -> bool:
   if not _entityStates[targetId] or not _entityStates[targetId][stateId]:
      return False

   return _entityStates[targetId][stateId] > 0
   
def getStates(targetId:float) -> list:
   stateId = None
   states:list = list()
   if not _entityStates[targetId]:
      return states

   for stateId in _entityStates[targetId]:
      if _entityStates[targetId][stateId] > 0:
         states.append(stateId)

   return states

def getStatus(targetId:float) -> FighterStatus:
   stateId = None
   state:SpellState = None
   fighterstatus:FighterStatus = FighterStatus()
   for stateId in _entityStates[targetId]:

      state = SpellState.getSpellStateById(stateId)
      if state and _entityStates[targetId][stateId] > 0:
         if state.preventsSpellCast:
            fighterstatus.cantUseSpells = True

         if state.preventsFight:
            fighterstatus.cantUseCloseQuarterAttack = True

         if state.cantDealDamage:
            fighterstatus.cantDealDamage = True

         if state.invulnerable:
            fighterstatus.invulnerable = True

         if state.incurable:
            fighterstatus.incurable = True

         if state.cantBeMoved:
            fighterstatus.cantBeMoved = True

         if state.cantBeappended:
            fighterstatus.cantBeappended = True

         if state.cantSwitchPosition:
            fighterstatus.cantSwitchPosition = True

         if state.invulnerableMelee:
            fighterstatus.invulnerableMelee = True

         if state.invulnerableRange:
            fighterstatus.invulnerableRange = True

         if state.cantTackle:
            fighterstatus.cantTackle = True

         if state.cantBeTackled:
            fighterstatus.cantBeTackled = True

   return fighterstatus

def endFight() -> None:
   _entityStates = dict()



