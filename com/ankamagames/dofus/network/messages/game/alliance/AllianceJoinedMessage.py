from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


class AllianceJoinedMessage(NetworkMessage):
    protocolId = 1981
    allianceInfo:AllianceInformations
    enabled:bool
    leadingGuildId:int
    
    
