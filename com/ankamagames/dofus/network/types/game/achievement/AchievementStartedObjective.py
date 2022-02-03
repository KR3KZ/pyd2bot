from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective


class AchievementStartedObjective(AchievementObjective):
    value:int
    

    def init(self, value:int, id:int, maxValue:int):
        self.value = value
        
        super().__init__(id, maxValue)
    
    