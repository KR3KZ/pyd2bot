from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapNoMovementMessage(NetworkMessage):
    cellX:int
    cellY:int
    

    def init(self, cellX:int, cellY:int):
        self.cellX = cellX
        self.cellY = cellY
        
        super().__init__()
    
    