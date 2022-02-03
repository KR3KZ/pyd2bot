      
class PVPRankItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      return I18n.getUiText("ui.pvp.rank") + " " + _operator.text + " " + _criterionValue
   
   def clone(self) -> IItemCriterion:
      return PVPRankItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return 0
