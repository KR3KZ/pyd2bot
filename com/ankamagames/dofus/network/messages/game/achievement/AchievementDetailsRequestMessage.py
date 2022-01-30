from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AchievementDetailsRequestMessage(NetworkMessage):
    protocolId = 5136
    achievementId:int
    
    
