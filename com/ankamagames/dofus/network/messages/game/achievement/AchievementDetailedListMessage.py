from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


class AchievementDetailedListMessage(NetworkMessage):
    startedAchievements:list[Achievement]
    finishedAchievements:list[Achievement]
    
    
