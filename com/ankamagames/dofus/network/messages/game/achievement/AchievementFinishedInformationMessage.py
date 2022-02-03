from com.ankamagames.dofus.network.messages.game.achievement.AchievementFinishedMessage import AchievementFinishedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.AchievementAchievedRewardable import AchievementAchievedRewardable
    


class AchievementFinishedInformationMessage(AchievementFinishedMessage):
    name:str
    playerId:int
    

    def init(self, name:str, playerId:int, achievement:'AchievementAchievedRewardable'):
        self.name = name
        self.playerId = playerId
        
        super().__init__(achievement)
    
    