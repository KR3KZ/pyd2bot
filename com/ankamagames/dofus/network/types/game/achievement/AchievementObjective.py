from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AchievementObjective(NetworkMessage):
    id:int
    maxValue:int
    

    def init(self, id:int, maxValue:int):
        self.id = id
        self.maxValue = maxValue
        
        super().__init__()
    
    