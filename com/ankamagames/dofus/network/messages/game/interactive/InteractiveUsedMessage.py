from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class InteractiveUsedMessage(NetworkMessage):
    entityId:int
    elemId:int
    skillId:int
    duration:int
    canMove:bool
    

    def init(self, entityId:int, elemId:int, skillId:int, duration:int, canMove:bool):
        self.entityId = entityId
        self.elemId = elemId
        self.skillId = skillId
        self.duration = duration
        self.canMove = canMove
        
        super().__init__()
    
    