from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.AchievementAchievedRewardable import AchievementAchievedRewardable
    


class AchievementFinishedMessage(NetworkMessage):
    achievement:'AchievementAchievedRewardable'
    

    def init(self, achievement:'AchievementAchievedRewardable'):
        self.achievement = achievement
        
        super().__init__()
    
    