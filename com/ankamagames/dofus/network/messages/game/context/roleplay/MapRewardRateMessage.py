from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MapRewardRateMessage(INetworkMessage):
    protocolId = 1514
    mapRate:int
    subAreaRate:int
    totalRate:int
    
    
