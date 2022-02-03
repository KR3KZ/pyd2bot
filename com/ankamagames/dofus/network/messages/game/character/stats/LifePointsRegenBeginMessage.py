from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LifePointsRegenBeginMessage(NetworkMessage):
    regenRate:int
    

    def init(self, regenRate:int):
        self.regenRate = regenRate
        
        super().__init__()
    
    