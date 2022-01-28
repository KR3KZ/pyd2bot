         


from pyd2bot.dofus.datacenter.items.GroupItemCriterion import GroupItemCriterion
from pyd2bot.dofus.datacenter.monsters.monster import Monster


class MonsterDropCoefficient:
      
   
   monsterId:int
   
   monsterGrade:int
   
   dropCoefficient:float
   
   criteria:str
   
   _monster:Monster
   
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
