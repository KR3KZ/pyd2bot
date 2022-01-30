from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildCreationResultMessage(INetworkMessage):
    protocolId = 42
    result:int
    
    
