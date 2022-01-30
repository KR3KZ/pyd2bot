from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AchievementAchieved(INetworkMessage):
    protocolId = 1836
    id:int
    achievedBy:int
    
    
