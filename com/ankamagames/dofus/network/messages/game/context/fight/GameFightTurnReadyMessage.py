from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnReadyMessage(NetworkMessage):
    isReady:bool
    

    def init(self, isReady:bool):
        self.isReady = isReady
        
        super().__init__()
    
    