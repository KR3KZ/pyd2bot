from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AchievementRewardErrorMessage(NetworkMessage):
    protocolId = 8883
    achievementId:int
    
    
