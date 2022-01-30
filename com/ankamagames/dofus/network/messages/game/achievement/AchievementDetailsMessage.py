from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.achievement.Achievement import Achievement


class AchievementDetailsMessage(NetworkMessage):
    protocolId = 5303
    achievement:Achievement
    
