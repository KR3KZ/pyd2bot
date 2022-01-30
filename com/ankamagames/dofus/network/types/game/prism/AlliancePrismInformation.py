from com.ankamagames.dofus.network.types.game.prism.PrismInformation import PrismInformation
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


class AlliancePrismInformation(PrismInformation):
    protocolId = 1469
    alliance:AllianceInformations
    
    
