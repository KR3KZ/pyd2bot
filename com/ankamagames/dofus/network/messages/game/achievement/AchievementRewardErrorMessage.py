from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AchievementRewardErrorMessage(INetworkMessage):
    protocolId = 8883
    achievementId:int
    
    
