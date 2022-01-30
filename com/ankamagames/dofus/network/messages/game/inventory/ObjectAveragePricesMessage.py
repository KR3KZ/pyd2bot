from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ObjectAveragePricesMessage(NetworkMessage):
    protocolId = 5921
    ids:int
    avgPrices:int
    
    
