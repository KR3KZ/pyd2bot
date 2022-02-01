from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PaddockBuyRequestMessage(INetworkMessage):
    protocolId = 8638
    proposedPrice:int
    
    
