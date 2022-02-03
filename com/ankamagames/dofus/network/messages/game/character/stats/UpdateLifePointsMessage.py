from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateLifePointsMessage(NetworkMessage):
    lifePoints:int
    maxLifePoints:int
    

    def init(self, lifePoints:int, maxLifePoints:int):
        self.lifePoints = lifePoints
        self.maxLifePoints = maxLifePoints
        
        super().__init__()
    
    