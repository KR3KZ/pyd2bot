from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GuildEmblem(INetworkMessage):
    protocolId = 2994
    symbolShape:int
    symbolColor:int
    backgroundShape:int
    backgroundColor:int
    
    
