from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameActionMarkedCell(INetworkMessage):
    protocolId = 2389
    cellId:int
    zoneSize:int
    cellColor:int
    cellsType:int
    
    
