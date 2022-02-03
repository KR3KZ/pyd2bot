from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShowCellMessage(NetworkMessage):
    sourceId:int
    cellId:int
    

    def init(self, sourceId:int, cellId:int):
        self.sourceId = sourceId
        self.cellId = cellId
        
        super().__init__()
    
    