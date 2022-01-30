from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


class AchievementAlmostFinishedDetailedListMessage(INetworkMessage):
    protocolId = 6475
    almostFinishedAchievements:Achievement
    
    
