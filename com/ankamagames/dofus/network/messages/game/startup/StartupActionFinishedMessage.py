from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StartupActionFinishedMessage(NetworkMessage):
    actionId:int
    success:bool
    automaticAction:bool
    

    def init(self, actionId:int):
        self.actionId = actionId
        
        super().__init__()
    
    