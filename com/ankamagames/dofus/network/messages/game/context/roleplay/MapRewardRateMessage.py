from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MapRewardRateMessage(NetworkMessage):
    protocolId = 1514
    mapRate:int
    subAreaRate:int
    totalRate:int
    
    
