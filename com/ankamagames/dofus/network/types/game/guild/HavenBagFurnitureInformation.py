from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HavenBagFurnitureInformation(NetworkMessage):
    cellId:int
    funitureId:int
    orientation:int
    

    def init(self, cellId:int, funitureId:int, orientation:int):
        self.cellId = cellId
        self.funitureId = funitureId
        self.orientation = orientation
        
        super().__init__()
    
    