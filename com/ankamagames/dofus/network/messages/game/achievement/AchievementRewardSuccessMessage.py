from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AchievementRewardSuccessMessage(INetworkMessage):
    protocolId = 2669
    achievementId:int
    
    
