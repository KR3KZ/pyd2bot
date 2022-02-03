from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectEffect(NetworkMessage):
    actionId:int
    

    def init(self, actionId:int):
        self.actionId = actionId
        
        super().__init__()
    
    