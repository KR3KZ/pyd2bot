from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StatedElement(NetworkMessage):
    elementId:int
    elementCellId:int
    elementState:int
    onCurrentMap:bool
    

    def init(self, elementId:int, elementCellId:int, elementState:int, onCurrentMap:bool):
        self.elementId = elementId
        self.elementCellId = elementCellId
        self.elementState = elementState
        self.onCurrentMap = onCurrentMap
        
        super().__init__()
    
    