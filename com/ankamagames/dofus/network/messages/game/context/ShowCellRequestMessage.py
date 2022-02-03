from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ShowCellRequestMessage(NetworkMessage):
    cellId:int
    

    def init(self, cellId:int):
        self.cellId = cellId
        
        super().__init__()
    
    