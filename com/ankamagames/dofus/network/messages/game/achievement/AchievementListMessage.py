from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved


class AchievementListMessage(NetworkMessage):
    protocolId = 4607
    finishedAchievements:AchievementAchieved
    
