from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AchievementRewardRequestMessage(NetworkMessage):
    protocolId = 3165
    achievementId:int
    
