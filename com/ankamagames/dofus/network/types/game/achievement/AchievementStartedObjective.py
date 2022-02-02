from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective


@dataclass
class AchievementStartedObjective(AchievementObjective):
    value:int
    
    
    def __post_init__(self):
        super().__init__()
    