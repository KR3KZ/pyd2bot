from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AchievementObjective(NetworkMessage):
    protocolId = 8917
    id:int
    maxValue:int
    
