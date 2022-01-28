from com.ankamagames.dofus.datacenter.items.criterion.GroupItemCriterion import GroupItemCriterion
from typing import TYPE_CHECKING
if TYPE_CHECKING:
   from com.ankamagames.dofus.datacenter.monsters.monsterGrade import MonsterGrade
from com.ankamagames.dofus.types.idAccessors import IdAccessors
from com.ankamagames.jerakine.data import I18n
from com.ankamagames.jerakine.data.gameData import GameData


class MonsterRace:
   
   MODULE:str = "MonsterRaces"
      
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
   def getMonsterRaceById(id:int) -> 'MonsterGrade':
      return GameData.getObject(MonsterRace.MODULE,id)
   
   @staticmethod
   def getMonsterRaces() -> list:
      return GameData.getObjects(MonsterRace.MODULE)

   idAccessors:IdAccessors = IdAccessors(getMonsterRaceById, getMonsterRaces)
   
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
