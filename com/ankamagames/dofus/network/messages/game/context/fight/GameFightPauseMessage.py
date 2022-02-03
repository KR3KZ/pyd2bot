from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPauseMessage(NetworkMessage):
    isPaused:bool
    

    def init(self, isPaused:bool):
        self.isPaused = isPaused
        
        super().__init__()
    
    