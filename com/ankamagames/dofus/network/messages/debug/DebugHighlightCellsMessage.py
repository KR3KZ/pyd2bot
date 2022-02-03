from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebugHighlightCellsMessage(NetworkMessage):
    color:int
    cells:list[int]
    

    def init(self, color:int, cells:list[int]):
        self.color = color
        self.cells = cells
        
        super().__init__()
    
    