

from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionFactory import ItemCriterionFactory


class AccountRightsItemCriterion(ItemCriterion):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   def clone(self) -> ItemCriterionFactory:
      return AccountRightsItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return 0
