from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AchievementRewardRequestMessage(INetworkMessage):
    protocolId = 3165
    achievementId:int
    
    
