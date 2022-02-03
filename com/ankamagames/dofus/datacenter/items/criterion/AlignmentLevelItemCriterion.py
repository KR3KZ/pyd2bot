               
class AlignmentLevelItemCriterion(ItemCriterion, IDataCenter):
      
   
   def __init__(self, pCriterion:str):
      super().__init__(pCriterion)
   
   @property
   def text(self) -> str:
      readableCriterionRef:str = I18n.getUiText("ui.tooltip.AlignmentLevel")
      return readableCriterionRef + " " + _operator.text + " " + _criterionValue
   
   def clone(self) -> IItemCriterion:
      return AlignmentLevelItemCriterion(self.basicText)
   
   def getCriterion(self) -> int:
      alignInfo:ActorExtendedAlignmentInformations = PlayedCharacterManager().characteristics.alignmentInfos
      return alignInfo.alignmentValue
