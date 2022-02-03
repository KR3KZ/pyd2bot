from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityDispositionInformations(NetworkMessage):
    cellId:int
    direction:int
    

    def init(self, cellId:int, direction:int):
        self.cellId = cellId
        self.direction = direction
        
        super().__init__()
    
    