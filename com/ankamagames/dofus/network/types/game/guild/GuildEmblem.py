from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GuildEmblem(INetworkMessage):
    protocolId = 2994
    symbolShape:int
    symbolColor:int
    backgroundShape:int
    backgroundColor:int
    
    
