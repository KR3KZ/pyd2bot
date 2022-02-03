from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapChangeOrientationRequestMessage(NetworkMessage):
    direction:int
    

    def init(self, direction:int):
        self.direction = direction
        
        super().__init__()
    
    