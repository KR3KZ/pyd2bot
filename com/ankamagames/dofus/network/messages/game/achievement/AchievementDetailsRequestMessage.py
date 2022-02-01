from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AchievementDetailsRequestMessage(INetworkMessage):
    protocolId = 5136
    achievementId:int
    
    
