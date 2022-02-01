from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


class AchievementAlmostFinishedDetailedListMessage(NetworkMessage):
    almostFinishedAchievements:list[Achievement]
    
    
