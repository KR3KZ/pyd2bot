from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


@dataclass
class AlliancePrismInformation(PrismInformation):
    alliance:AllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    