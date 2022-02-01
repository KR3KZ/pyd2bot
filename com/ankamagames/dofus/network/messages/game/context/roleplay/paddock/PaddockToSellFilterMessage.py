from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockToSellFilterMessage(NetworkMessage):
    areaId:int
    atLeastNbMount:int
    atLeastNbMachine:int
    maxPrice:int
    orderBy:int
    
    
