               
class AlignmentItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      readableCriterionValue:str = AlignmentSide.getAlignmentSideById(int(_criterionValue)).name
      readableCriterionRef:str = I18n.getUiText("ui.common.alignment")
      readableOperator:str = ":"
      if _operator.text == ItemCriterionOperator.DIFFERENT:
         readableOperator = I18n.getUiText("ui.common.differentFrom") + I18n.getUiText("ui.common.colon")
      return readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
   
   def clone(self) -> IItemCriterion:
      return AlignmentItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      return PlayedCharacterManager().characteristics.alignmentInfos.alignmentSide
