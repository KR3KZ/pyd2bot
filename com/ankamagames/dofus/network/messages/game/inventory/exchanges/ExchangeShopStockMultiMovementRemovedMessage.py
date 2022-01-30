from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeShopStockMultiMovementRemovedMessage(INetworkMessage):
    protocolId = 3309
    objectIdList:int
    
    
