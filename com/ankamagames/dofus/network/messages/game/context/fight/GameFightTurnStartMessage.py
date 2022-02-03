from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnStartMessage(NetworkMessage):
    id:int
    waitTime:int
    

    def init(self, id:int, waitTime:int):
        self.id = id
        self.waitTime = waitTime
        
        super().__init__()
    
    