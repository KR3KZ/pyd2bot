from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EmotePlayAbstractMessage(INetworkMessage):
    protocolId = 4497
    emoteId:int
    emoteStartTime:int
    
    
