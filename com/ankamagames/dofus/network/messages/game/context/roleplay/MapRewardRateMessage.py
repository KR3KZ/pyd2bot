from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MapRewardRateMessage(NetworkMessage):
    mapRate:int
    subAreaRate:int
    totalRate:int
    
    
