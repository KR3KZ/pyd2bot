from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AchievementAchieved(NetworkMessage):
    protocolId = 1836
    id:int
    achievedBy:int
    
    
