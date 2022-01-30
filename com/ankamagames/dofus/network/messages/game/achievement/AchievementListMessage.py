from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.AchievementAchieved import AchievementAchieved


class AchievementListMessage(INetworkMessage):
    protocolId = 4607
    finishedAchievements:AchievementAchieved
    
    
