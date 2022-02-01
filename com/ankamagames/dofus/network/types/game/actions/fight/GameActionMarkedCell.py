from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameActionMarkedCell(NetworkMessage):
    cellId:int
    zoneSize:int
    cellColor:int
    cellsType:int
    
    
