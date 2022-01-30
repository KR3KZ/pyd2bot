from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeBidHousePriceMessage(INetworkMessage):
    protocolId = 8992
    genId:int
    
    
