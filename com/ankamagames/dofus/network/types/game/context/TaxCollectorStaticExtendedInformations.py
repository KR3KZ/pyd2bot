from com.ankamagames.dofus.network.types.game.context.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


class TaxCollectorStaticExtendedInformations(TaxCollectorStaticInformations):
    protocolId = 6505
    allianceIdentity:AllianceInformations
    
