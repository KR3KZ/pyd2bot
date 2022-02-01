from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AchievementObjective(INetworkMessage):
    protocolId = 8917
    id:int
    maxValue:int
    
    
