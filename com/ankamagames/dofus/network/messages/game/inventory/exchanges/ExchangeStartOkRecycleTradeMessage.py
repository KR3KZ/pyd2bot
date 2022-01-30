from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkRecycleTradeMessage(NetworkMessage):
    protocolId = 9169
    percentToPrism:int
    percentToPlayer:int
    
    
