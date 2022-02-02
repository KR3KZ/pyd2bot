from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


@dataclass
class AchievementDetailedListMessage(NetworkMessage):
    startedAchievements:list[Achievement]
    finishedAchievements:list[Achievement]
    
    
    def __post_init__(self):
        super().__init__()
    