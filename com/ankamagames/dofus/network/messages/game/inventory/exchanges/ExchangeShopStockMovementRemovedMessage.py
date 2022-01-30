from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeShopStockMovementRemovedMessage(NetworkMessage):
    protocolId = 7025
    objectId:int
    
    
