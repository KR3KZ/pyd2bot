from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PaddockToSellFilterMessage(NetworkMessage):
    protocolId = 8388
    areaId:int
    atLeastNbMount:int
    atLeastNbMachine:int
    maxPrice:int
    orderBy:int
    
    
