from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceGuildLeavingMessage(INetworkMessage):
    protocolId = 129
    kicked:bool
    guildId:int
    
    
