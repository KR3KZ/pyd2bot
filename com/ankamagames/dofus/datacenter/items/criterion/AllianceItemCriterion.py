               
   class AllianceItemCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         if _criterionValue == 0:
            return I18n.getUiText("ui.criterion.noAlliance")
         return I18n.getUiText("ui.criterion.hasAlliance")
      
      def clone(self) -> IItemCriterion:
         return AllianceItemCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         alliance:AllianceWrapper = AllianceFrame().alliance
         if alliance:
            return 1
         return 0
