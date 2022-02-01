from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectAveragePricesMessage(NetworkMessage):
    ids:list[int]
    avgPrices:list[int]
    
    
