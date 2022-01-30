from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class HouseToSellFilterMessage(NetworkMessage):
    protocolId = 3571
    areaId:int
    atLeastNbRoom:int
    atLeastNbChest:int
    skillRequested:int
    maxPrice:float
    orderBy:int
    
