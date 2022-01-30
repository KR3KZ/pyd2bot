from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameActionMarkedCell(NetworkMessage):
    protocolId = 2389
    cellId:int
    zoneSize:int
    cellColor:int
    cellsType:int
    
