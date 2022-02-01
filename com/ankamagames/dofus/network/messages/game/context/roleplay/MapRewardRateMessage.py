from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MapRewardRateMessage(INetworkMessage):
    protocolId = 1514
    mapRate:int
    subAreaRate:int
    totalRate:int
    
    
