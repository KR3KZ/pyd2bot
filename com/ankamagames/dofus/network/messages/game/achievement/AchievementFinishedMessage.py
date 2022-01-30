from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchievedRewardable import AchievementAchievedRewardable


class AchievementFinishedMessage(NetworkMessage):
    protocolId = 8970
    achievement:AchievementAchievedRewardable
    
