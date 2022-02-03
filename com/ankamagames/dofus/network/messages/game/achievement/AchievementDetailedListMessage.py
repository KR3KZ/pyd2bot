from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
    from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
    


class AchievementDetailedListMessage(NetworkMessage):
    startedAchievements:list['Achievement']
    finishedAchievements:list['Achievement']
    

    def init(self, startedAchievements:list['Achievement'], finishedAchievements:list['Achievement']):
        self.startedAchievements = startedAchievements
        self.finishedAchievements = finishedAchievements
        
        super().__init__()
    
    