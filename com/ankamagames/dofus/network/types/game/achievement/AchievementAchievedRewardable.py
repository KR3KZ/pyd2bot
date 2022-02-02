from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved


@dataclass
class AchievementAchievedRewardable(AchievementAchieved):
    finishedlevel:int
    
    
    def __post_init__(self):
        super().__init__()
    