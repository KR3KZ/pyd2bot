from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.achievement.AchievementFinishedMessage import AchievementFinishedMessage


@dataclass
class AchievementFinishedInformationMessage(AchievementFinishedMessage):
    name:str
    playerId:int
    
    
    def __post_init__(self):
        super().__init__()
    