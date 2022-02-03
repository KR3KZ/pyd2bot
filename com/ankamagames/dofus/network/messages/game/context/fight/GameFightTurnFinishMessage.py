from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightTurnFinishMessage(NetworkMessage):
    isAfk:bool
    

    def init(self, isAfk:bool):
        self.isAfk = isAfk
        
        super().__init__()
    
    