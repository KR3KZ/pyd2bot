                  
from pyd2bot.dofus.datacenter.items.GroupItemCriterion import GroupItemCriterion
from pyd2bot.dofus.datacenter.monsters.MonsterGrade import MonsterGrade
from pyd2bot.gameData.IdAccessors import IdAccessors
from pyd2bot.jerakine.data.I18n import I18n


class MonsterRace:
   
   MODULE:str = "MonsterRaces"
   
   idAccessors:IdAccessors = IdAccessors(MonsterRace.getMonsterRaceById, MonsterRace.getMonsterRaces)
      
   
   id:int
   
   superRaceId:int
   
   nameId:int
   
   monsters:list[int]
   
   aggressiveZoneSize:int
   
   aggressiveLevelDiff:int
   
   aggressiveImmunityCriterion:str
   
   aggressiveAttackDelay:int
   
   _name:str
   
   def __init__(self):
      super().__init__()
   
   @staticmethod
   def getMonsterRaceById(id:int) -> MonsterGrade:
      return GameData.getObject(MonsterRace.MODULE,id)
   
   @staticmethod
   def getMonsterRaces() -> list:
      return GameData.getObjects(MonsterRace.MODULE)
   
   @property
   def name(self) -> str:
      if not self._name:
         self._name = I18n.getText(self.nameId)
      return self._name
   
   @property
   def canAttack(self) -> bool:
      criterions:GroupItemCriterion = None
      if self.aggressiveImmunityCriterion:
         criterions = GroupItemCriterion(self.aggressiveImmunityCriterion)
         if criterions.isRespected:
            return False
      return True
