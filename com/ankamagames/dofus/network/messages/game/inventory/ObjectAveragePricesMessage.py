from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectAveragePricesMessage(INetworkMessage):
    protocolId = 5921
    ids:int
    avgPrices:int
    
    
