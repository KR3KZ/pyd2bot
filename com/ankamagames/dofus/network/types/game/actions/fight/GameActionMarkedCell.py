from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameActionMarkedCell(INetworkMessage):
    protocolId = 2389
    cellId:int
    zoneSize:int
    cellColor:int
    cellsType:int
    
    
