      
class RuneByBreakingItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      readableCriterionValue:str = _criterionValueText
      runeBybreakingItem:int = parseInt(readableCriterionValue.split(",")[1]) + 1
      return I18n.getUiText("ui.smithmagic.runeByBreakingItemCriterion",[runeBybreakingItem])
   
   def clone(self) -> IItemCriterion:
      return MonsterGroupChallengeCriterion(self.basicText)
