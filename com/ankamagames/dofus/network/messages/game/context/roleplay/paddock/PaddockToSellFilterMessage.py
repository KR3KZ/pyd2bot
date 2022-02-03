from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockToSellFilterMessage(NetworkMessage):
    areaId:int
    atLeastNbMount:int
    atLeastNbMachine:int
    maxPrice:int
    orderBy:int
    

    def init(self, areaId:int, atLeastNbMount:int, atLeastNbMachine:int, maxPrice:int, orderBy:int):
        self.areaId = areaId
        self.atLeastNbMount = atLeastNbMount
        self.atLeastNbMachine = atLeastNbMachine
        self.maxPrice = maxPrice
        self.orderBy = orderBy
        
        super().__init__()
    
    