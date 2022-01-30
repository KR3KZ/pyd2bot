from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidPriceMessage(NetworkMessage):
    protocolId = 8533
    genericId:int
    averagePrice:int
    
    
