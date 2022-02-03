from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockMoveItemRequestMessage(NetworkMessage):
    oldCellId:int
    newCellId:int
    

    def init(self, oldCellId:int, newCellId:int):
        self.oldCellId = oldCellId
        self.newCellId = newCellId
        
        super().__init__()
    
    