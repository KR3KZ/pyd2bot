from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeBidHousePriceMessage(INetworkMessage):
    protocolId = 8992
    genId:int
    
    
