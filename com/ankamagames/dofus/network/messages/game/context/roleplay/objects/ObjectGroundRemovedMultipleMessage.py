from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectGroundRemovedMultipleMessage(NetworkMessage):
    cells:list[int]
    

    def init(self, cells:list[int]):
        self.cells = cells
        
        super().__init__()
    
    