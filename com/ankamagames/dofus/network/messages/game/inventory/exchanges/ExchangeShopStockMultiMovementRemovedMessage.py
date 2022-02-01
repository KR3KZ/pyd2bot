from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeShopStockMultiMovementRemovedMessage(INetworkMessage):
    protocolId = 3309
    objectIdList:int
    
    
