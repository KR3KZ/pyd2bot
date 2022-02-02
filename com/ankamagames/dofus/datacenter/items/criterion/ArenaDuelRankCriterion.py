               
   class ArenaDuelRankCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = str(_criterionValue)
         readableCriterionRef:str = I18n.getUiText("ui.common.pvpDuelRank")
         readableOperator = ">"
         if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText("ui.common.differentFrom") + " >"
         return readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
      
      def clone(self) -> IItemCriterion:
         return ArenaDuelRankCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         frame:PartyManagementFrame =Kernel().getWorker().getFrame(PartyManagementFrame)
         rank:int = 0
         if frame.arenaRankDuelInfos and frame.arenaRankDuelInfos.rank > rank:
            rank = frame.arenaRankDuelInfos.rank
         return rank
