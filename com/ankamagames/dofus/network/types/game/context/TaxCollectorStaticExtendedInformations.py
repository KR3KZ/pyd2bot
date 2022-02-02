from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


@dataclass
class TaxCollectorStaticExtendedInformations(TaxCollectorStaticInformations):
    allianceIdentity:AllianceInformations
    
    
    def __post_init__(self):
        super().__init__()
    