from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ItemForPreset(NetworkMessage):
    position:int
    objGid:int
    objUid:int
    

    def init(self, position:int, objGid:int, objUid:int):
        self.position = position
        self.objGid = objGid
        self.objUid = objUid
        
        super().__init__()
    
    