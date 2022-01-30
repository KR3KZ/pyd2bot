from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeShopStockMultiMovementRemovedMessage(NetworkMessage):
    protocolId = 3309
    objectIdList:int
    
