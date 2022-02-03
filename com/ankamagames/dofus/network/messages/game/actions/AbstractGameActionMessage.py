from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AbstractGameActionMessage(NetworkMessage):
    actionId:int
    sourceId:int
    

    def init(self, actionId:int, sourceId:int):
        self.actionId = actionId
        self.sourceId = sourceId
        
        super().__init__()
    
    