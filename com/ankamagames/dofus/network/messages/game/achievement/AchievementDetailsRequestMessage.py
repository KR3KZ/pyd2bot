from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AchievementDetailsRequestMessage(INetworkMessage):
    protocolId = 5136
    achievementId:int
    
    
