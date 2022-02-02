               
   class ArenaMaxDuelRankCriterion(ItemCriterion implements IDataCenter):
       
      
      def __init__(self, pCriterion:str):
         super().__init__(pCriterion)
      
      @property
      def text(self) -> str:
         readableCriterionValue:str = str(_criterionValue)
         readableCriterionRef:str = I18n.getUiText("ui.common.pvpMaxDuelRank")
         readableOperator = ">"
         if _operator.text == ItemCriterionOperator.DIFFERENT:
            readableOperator = I18n.getUiText("ui.common.differentFrom") + " >"
         return readableCriterionRef + " " + readableOperator + " " + readableCriterionValue
      
      def clone(self) -> IItemCriterion:
         return ArenaMaxDuelRankCriterion(self.basicText)
      
      def getCriterion(self) -> int:
         frame:PartyManagementFrame =Kernel().getWorker().getFrame(PartyManagementFrame)
         maxRank:int = 0
         if frame.arenaRankDuelInfos and frame.arenaRankDuelInfos.maxRank > maxRank:
            maxRank = frame.arenaRankDuelInfos.maxRank
         return maxRank
