            
   class LevelItemCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = str(_criterionValue)
         readableCriterionRef:str = I18n.getUiText("ui.common.level")
         if _operator.text == ItemCriterionOperator.SUPERIOR:
            return I18n.getUiText("ui.common.minimumLevelCondition",[(_criterionValue + str(1))])
         if _operator.text == ItemCriterionOperator.INFERIOR:
            return I18n.getUiText("ui.common.maximumLevelCondition",[(_criterionValue - str(1))])
         return readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
      
      def clone(self) -> IItemCriterion:
         return LevelItemCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         return PlayedCharacterManager().limitedLevel
