         
   class MonsterGroupChallengeCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = str(_criterionValue + 1)
         return I18n.getUiText("ui.breachReward.groupChallengCriterion",[readableCriterionValue])
      
      def clone(self) -> IItemCriterion:
         return MonsterGroupChallengeCriterion(self.basicText)
