from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AchievementRewardSuccessMessage(INetworkMessage):
    protocolId = 2669
    achievementId:int
    
    
