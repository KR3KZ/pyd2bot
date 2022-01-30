from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceGuildLeavingMessage(INetworkMessage):
    protocolId = 129
    kicked:bool
    guildId:int
    
    
