from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseToSellFilterMessage(NetworkMessage):
    areaId:int
    atLeastNbRoom:int
    atLeastNbChest:int
    skillRequested:int
    maxPrice:int
    orderBy:int
    

    def init(self, areaId:int, atLeastNbRoom:int, atLeastNbChest:int, skillRequested:int, maxPrice:int, orderBy:int):
        self.areaId = areaId
        self.atLeastNbRoom = atLeastNbRoom
        self.atLeastNbChest = atLeastNbChest
        self.skillRequested = skillRequested
        self.maxPrice = maxPrice
        self.orderBy = orderBy
        
        super().__init__()
    
    