from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class EntityTalkMessage(NetworkMessage):
    entityId:int
    textId:int
    parameters:list[str]
    

    def init(self, entityId:int, textId:int, parameters:list[str]):
        self.entityId = entityId
        self.textId = textId
        self.parameters = parameters
        
        super().__init__()
    
    