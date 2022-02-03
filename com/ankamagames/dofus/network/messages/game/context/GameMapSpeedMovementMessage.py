from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapSpeedMovementMessage(NetworkMessage):
    speedMultiplier:int
    

    def init(self, speedMultiplier:int):
        self.speedMultiplier = speedMultiplier
        
        super().__init__()
    
    