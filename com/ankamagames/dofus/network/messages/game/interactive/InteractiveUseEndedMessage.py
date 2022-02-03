from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveUseEndedMessage(NetworkMessage):
    elemId:int
    skillId:int
    

    def init(self, elemId:int, skillId:int):
        self.elemId = elemId
        self.skillId = skillId
        
        super().__init__()
    
    