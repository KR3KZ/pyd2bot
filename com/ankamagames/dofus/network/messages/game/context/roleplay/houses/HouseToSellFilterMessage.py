from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseToSellFilterMessage(NetworkMessage):
    areaId:int
    atLeastNbRoom:int
    atLeastNbChest:int
    skillRequested:int
    maxPrice:int
    orderBy:int
    
    
