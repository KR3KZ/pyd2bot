from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeShopStockMultiMovementRemovedMessage(NetworkMessage):
    objectIdList:list[int]
    
    
