from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchievedRewardable import AchievementAchievedRewardable


class AchievementFinishedMessage(NetworkMessage):
    achievement:AchievementAchievedRewardable
    
    
