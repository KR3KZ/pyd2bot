from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeStartOkRecycleTradeMessage(INetworkMessage):
    protocolId = 9169
    percentToPrism:int
    percentToPlayer:int
    
    
