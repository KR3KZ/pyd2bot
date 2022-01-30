from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


class AchievementAlmostFinishedDetailedListMessage(NetworkMessage):
    protocolId = 6475
    almostFinishedAchievements:Achievement
    
    
