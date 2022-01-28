

from com.ankamagames.dofus.datacenter.items.criterion import GroupItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.MonsterGroupChallengeCriterion import MonsterGroupChallengeCriterion
from com.ankamagames.dofus.datacenter.monsters.monster import Monster
from com.ankamagames.dofus.datacenter.monsters.monsterDropCoefficient import MonsterDropCoefficient


class MonsterDrop:
      
   
   dropId:int
   
   monsterId:int
   
   objectId:int
   
   percentDropForGrade1:float
   
   percentDropForGrade2:float
   
   percentDropForGrade3:float
   
   percentDropForGrade4:float
   
   percentDropForGrade5:float
   
   count:int
   
   criteria:str
   
   hasCriteria:bool
   
   specificDropCoefficient:list[MonsterDropCoefficient]
   
   _monster:MonsterGroupChallengeCriterion
   
   _conditions:GroupItemCriterion
   
   def __init__(self):
      super().__init__()
   
   @property
   def monster(self) -> Monster:
      if not self._monster:
         self._monster = Monster.getMonsterById(self.monsterId)
      return self._monster
   
   @property
   def conditions(self) -> GroupItemCriterion:
      if not self.criteria:
         return None
      if not self._conditions:
         self._conditions = GroupItemCriterion(self.criteria)
      return self._conditions
   
   def getSpecificDropCoeffByGrade(self, grade:int) -> MonsterDropCoefficient:
      dropCoeff:MonsterDropCoefficient = None
      for dropCoeff in self.specificDropCoefficient:
         if grade == dropCoeff.monsterGrade:
            return dropCoeff
      return None
