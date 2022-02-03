         
class SubscribeItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      if _criterionValue == 1 and _operator.text == ItemCriterionOperator.EQUAL or _criterionValue == 0 and _operator.text == ItemCriterionOperator.DIFFERENT:
         return I18n.getUiText("ui.tooltip.beSubscirber")
      return I18n.getUiText("ui.tooltip.dontBeSubscriber")
   
   def clone(self) -> IItemCriterion:
      return SubscribeItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      timeRemaining:float = PlayerManager().subscriptionEndDate
      if timeRemaining > 0 or PlayerManager().hasRights:
         return 1
      return 0
