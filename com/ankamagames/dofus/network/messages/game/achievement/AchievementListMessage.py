from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved
    


class AchievementListMessage(NetworkMessage):
    finishedAchievements:list['AchievementAchieved']
    

    def init(self, finishedAchievements:list['AchievementAchieved']):
        self.finishedAchievements = finishedAchievements
        
        super().__init__()
    
    