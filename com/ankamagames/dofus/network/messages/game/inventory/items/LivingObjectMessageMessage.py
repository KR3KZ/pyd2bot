from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectMessageMessage(NetworkMessage):
    msgId:int
    timeStamp:int
    owner:str
    objectGenericId:int
    

    def init(self, msgId:int, timeStamp:int, owner:str, objectGenericId:int):
        self.msgId = msgId
        self.timeStamp = timeStamp
        self.owner = owner
        self.objectGenericId = objectGenericId
        
        super().__init__()
    
    