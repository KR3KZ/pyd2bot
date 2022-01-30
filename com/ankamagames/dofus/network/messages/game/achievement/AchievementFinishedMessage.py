from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchievedRewardable import AchievementAchievedRewardable


class AchievementFinishedMessage(INetworkMessage):
    protocolId = 8970
    achievement:AchievementAchievedRewardable
    
    
