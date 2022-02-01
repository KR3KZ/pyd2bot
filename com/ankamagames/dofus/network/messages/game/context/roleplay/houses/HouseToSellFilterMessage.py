from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class HouseToSellFilterMessage(INetworkMessage):
    protocolId = 3571
    areaId:int
    atLeastNbRoom:int
    atLeastNbChest:int
    skillRequested:int
    maxPrice:int
    orderBy:int
    
    
