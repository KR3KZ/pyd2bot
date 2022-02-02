from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved


@dataclass
class AchievementListMessage(NetworkMessage):
    finishedAchievements:list[AchievementAchieved]
    
    
    def __post_init__(self):
        super().__init__()
    