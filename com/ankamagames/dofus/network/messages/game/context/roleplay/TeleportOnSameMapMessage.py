from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TeleportOnSameMapMessage(NetworkMessage):
    targetId:int
    cellId:int
    

    def init(self, targetId:int, cellId:int):
        self.targetId = targetId
        self.cellId = cellId
        
        super().__init__()
    
    