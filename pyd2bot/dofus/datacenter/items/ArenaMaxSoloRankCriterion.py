               
   class ArenaMaxSoloRankCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = str(_criterionValue)
         readableCriterionRef:str = I18n.getUiText("ui.common.pvpMaxSoloRank")
         readableOperator = ">"
         if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText("ui.common.differentFrom") + " >"
         return readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
      
      def clone(self) -> IItemCriterion:
         return ArenaMaxSoloRankCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         frame:PartyManagementFrame = Kernel.getWorker().getFrame(PartyManagementFrame)
         return int(frame.arenaRankSoloInfos.maxRank)
