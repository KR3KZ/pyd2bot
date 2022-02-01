from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AchievementRewardErrorMessage(INetworkMessage):
    protocolId = 8883
    achievementId:int
    
    
