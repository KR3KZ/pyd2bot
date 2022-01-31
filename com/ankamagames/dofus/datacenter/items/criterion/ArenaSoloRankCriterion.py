from com.ankamagames.dofus.datacenter.items.criterion.IItemCriterion import IItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterion import ItemCriterion
from com.ankamagames.dofus.datacenter.items.criterion.ItemCriterionOperator import ItemCriterionOperator
from com.ankamagames.dofus.kernel.kernel import Kernel
from com.ankamagames.jerakine.data.I18n import I18n
from com.ankamagames.jerakine.interfaces.IDataCenter import IDataCenter


class ArenaSoloRankCriterion(ItemCriterion, IDataCenter):
       
      
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
         return frame and int(frame.arenaRankSoloInfos) ? int(frame.arenaRankSoloInfos.rank) : 0
