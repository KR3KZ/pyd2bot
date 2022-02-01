from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectAveragePricesMessage(INetworkMessage):
    protocolId = 5921
    ids:int
    avgPrices:int
    
    
