from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidPriceMessage(INetworkMessage):
    protocolId = 8533
    genericId:int
    averagePrice:int
    
    
