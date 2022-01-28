            
   class WeightItemCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = str(_criterionValue)
         readableCriterionRef:str = I18n.getUiText("ui.common.weight")
         return readableCriterionRef + " " + _operator.text + " " + readableCriterionValue
      
      def clone(self) -> IItemCriterion:
         return WeightItemCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         return PlayedCharacterManager().inventoryWeight
