from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LivingObjectMessageRequestMessage(NetworkMessage):
    msgId:int
    parameters:list[str]
    livingObject:int
    

    def init(self, msgId:int, parameters:list[str], livingObject:int):
        self.msgId = msgId
        self.parameters = parameters
        self.livingObject = livingObject
        
        super().__init__()
    
    