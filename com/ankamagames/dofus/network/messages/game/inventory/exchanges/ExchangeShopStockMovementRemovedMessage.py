from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeShopStockMovementRemovedMessage(INetworkMessage):
    protocolId = 7025
    objectId:int
    
    
