from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeSellMessage(INetworkMessage):
    protocolId = 5196
    objectToSellId:int
    quantity:int
    
    
