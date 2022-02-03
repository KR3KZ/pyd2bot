from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionAcknowledgementMessage(NetworkMessage):
    valid:bool
    actionId:int
    

    def init(self, valid:bool, actionId:int):
        self.valid = valid
        self.actionId = actionId
        
        super().__init__()
    
    