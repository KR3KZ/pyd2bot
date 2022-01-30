from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


class AchievementDetailedListMessage(INetworkMessage):
    protocolId = 9855
    startedAchievements:Achievement
    finishedAchievements:Achievement
    
    
