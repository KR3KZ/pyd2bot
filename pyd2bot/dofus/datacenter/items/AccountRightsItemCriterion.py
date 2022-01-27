            
from pyd2bot.dofus.datacenter.items.IItemCriterion import IItemCriterion
from pyd2bot.dofus.datacenter.items.ItemCriterion import ItemCriterion


class AccountRightsItemCriterion(ItemCriterion):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   def clone(self) -> IItemCriterion:
      return AccountRightsItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return 0
