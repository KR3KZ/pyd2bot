from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeShopStockMovementRemovedMessage(INetworkMessage):
    protocolId = 7025
    objectId:int
    
    
