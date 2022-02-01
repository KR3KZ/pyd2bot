from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeStartOkRecycleTradeMessage(INetworkMessage):
    protocolId = 9169
    percentToPrism:int
    percentToPlayer:int
    
    
