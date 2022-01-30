from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHousePriceMessage(NetworkMessage):
    protocolId = 8992
    genId:int
    
