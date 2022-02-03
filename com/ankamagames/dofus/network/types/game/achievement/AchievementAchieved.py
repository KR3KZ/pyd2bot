from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AchievementAchieved(NetworkMessage):
    id:int
    achievedBy:int
    

    def init(self, id:int, achievedBy:int):
        self.id = id
        self.achievedBy = achievedBy
        
        super().__init__()
    
    