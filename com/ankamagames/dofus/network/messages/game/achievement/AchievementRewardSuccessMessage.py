from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AchievementRewardSuccessMessage(NetworkMessage):
    protocolId = 2669
    achievementId:int
    
