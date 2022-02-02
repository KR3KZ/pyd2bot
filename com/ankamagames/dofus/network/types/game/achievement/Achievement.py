from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementObjective import AchievementObjective
from com.ankamagames.dofus.network.types.game.achievement.AchievementStartedObjective import AchievementStartedObjective


@dataclass
class Achievement(NetworkMessage):
    id:int
    finishedObjective:list[AchievementObjective]
    startedObjectives:list[AchievementStartedObjective]
    
    
    def __post_init__(self):
        super().__init__()
    