from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AchievementAchieved(INetworkMessage):
    protocolId = 1836
    id:int
    achievedBy:int
    
    
