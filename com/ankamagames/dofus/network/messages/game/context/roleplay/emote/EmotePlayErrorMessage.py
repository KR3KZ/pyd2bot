from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EmotePlayErrorMessage(INetworkMessage):
    protocolId = 9167
    emoteId:int
    
    
