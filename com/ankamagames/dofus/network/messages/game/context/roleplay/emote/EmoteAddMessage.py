from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EmoteAddMessage(INetworkMessage):
    protocolId = 8736
    emoteId:int
    
    
