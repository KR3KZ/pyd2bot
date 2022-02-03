from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved


class AchievementAchievedRewardable(AchievementAchieved):
    finishedlevel:int
    

    def init(self, finishedlevel:int, id:int, achievedBy:int):
        self.finishedlevel = finishedlevel
        
        super().__init__(id, achievedBy)
    
    