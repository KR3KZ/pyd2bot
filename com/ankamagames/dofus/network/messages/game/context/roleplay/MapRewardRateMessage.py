from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapRewardRateMessage(NetworkMessage):
    mapRate:int
    subAreaRate:int
    totalRate:int
    

    def init(self, mapRate:int, subAreaRate:int, totalRate:int):
        self.mapRate = mapRate
        self.subAreaRate = subAreaRate
        self.totalRate = totalRate
        
        super().__init__()
    
    