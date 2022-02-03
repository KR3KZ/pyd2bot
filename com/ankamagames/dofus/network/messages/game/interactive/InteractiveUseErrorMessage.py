from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveUseErrorMessage(NetworkMessage):
    elemId:int
    skillInstanceUid:int
    

    def init(self, elemId:int, skillInstanceUid:int):
        self.elemId = elemId
        self.skillInstanceUid = skillInstanceUid
        
        super().__init__()
    
    