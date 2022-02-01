from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved


class AchievementListMessage(NetworkMessage):
    finishedAchievements:list[AchievementAchieved]
    
    
