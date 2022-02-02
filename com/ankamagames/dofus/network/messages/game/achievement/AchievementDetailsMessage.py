from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


@dataclass
class AchievementDetailsMessage(NetworkMessage):
    achievement:Achievement
    
    
    def __post_init__(self):
        super().__init__()
    