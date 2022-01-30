from com.ankamagames.dofus.network.types.game.context.roleplay.HumanOption import HumanOption
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


class HumanOptionAlliance(HumanOption):
    protocolId = 3939
    allianceInformations:AllianceInformations
    aggressable:int
    
    
