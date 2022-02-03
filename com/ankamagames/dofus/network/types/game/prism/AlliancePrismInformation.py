from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations
    


class AlliancePrismInformation(PrismInformation):
    alliance:'AllianceInformations'
    

    def init(self, alliance:'AllianceInformations', typeId:int, state:int, nextVulnerabilityDate:int, placementDate:int, rewardTokenCount:int):
        self.alliance = alliance
        
        super().__init__(typeId, state, nextVulnerabilityDate, placementDate, rewardTokenCount)
    
    