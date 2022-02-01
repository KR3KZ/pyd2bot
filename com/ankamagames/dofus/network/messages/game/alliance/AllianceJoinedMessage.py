from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.AllianceInformations import AllianceInformations


class AllianceJoinedMessage(INetworkMessage):
    protocolId = 1981
    allianceInfo:AllianceInformations
    enabled:bool
    leadingGuildId:int
    
    
