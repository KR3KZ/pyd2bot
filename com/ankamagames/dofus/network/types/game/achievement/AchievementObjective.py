from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AchievementObjective(INetworkMessage):
    protocolId = 8917
    id:int
    maxValue:int
    
    
