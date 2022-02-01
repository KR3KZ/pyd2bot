from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AchievementRewardRequestMessage(INetworkMessage):
    protocolId = 3165
    achievementId:int
    
    
