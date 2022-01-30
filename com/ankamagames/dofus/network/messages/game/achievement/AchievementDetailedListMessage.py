from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


class AchievementDetailedListMessage(NetworkMessage):
    protocolId = 9855
    startedAchievements:Achievement
    finishedAchievements:Achievement
    
    
