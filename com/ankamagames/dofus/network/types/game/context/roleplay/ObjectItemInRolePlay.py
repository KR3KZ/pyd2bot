from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectItemInRolePlay(NetworkMessage):
    cellId:int
    objectGID:int
    

    def init(self, cellId:int, objectGID:int):
        self.cellId = cellId
        self.objectGID = objectGID
        
        super().__init__()
    
    