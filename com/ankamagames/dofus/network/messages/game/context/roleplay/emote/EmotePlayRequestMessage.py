from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class EmotePlayRequestMessage(INetworkMessage):
    protocolId = 5775
    emoteId:int
    
    
