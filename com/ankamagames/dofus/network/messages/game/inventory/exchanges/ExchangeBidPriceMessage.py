from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidPriceMessage(INetworkMessage):
    protocolId = 8533
    genericId:int
    averagePrice:int
    
    
