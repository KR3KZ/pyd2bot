               
   class ArenaSoloRankCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = str(_criterionValue)
         readableCriterionRef:str = I18n.getUiText("ui.common.pvpSoloRank")
         readableOperator = ">"
         if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText("ui.common.differentFrom") + " >"
         return readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
      
      def clone(self) -> IItemCriterion:
         return ArenaSoloRankCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         frame:PartyManagementFrame = Kernel.getWorker().getFrame(PartyManagementFrame)
         return int(frame and frame.arenaRankSoloInfos ? int(frame.arenaRankSoloInfos.rank) : 0)
