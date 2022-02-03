from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionMarkedCell(NetworkMessage):
    cellId:int
    zoneSize:int
    cellColor:int
    cellsType:int
    

    def init(self, cellId:int, zoneSize:int, cellColor:int, cellsType:int):
        self.cellId = cellId
        self.zoneSize = zoneSize
        self.cellColor = cellColor
        self.cellsType = cellsType
        
        super().__init__()
    
    