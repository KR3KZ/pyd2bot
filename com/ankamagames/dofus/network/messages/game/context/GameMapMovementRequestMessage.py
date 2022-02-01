from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameMapMovementRequestMessage(INetworkMessage):
    protocolId = 685
    keyMovements:int
    mapId:int
    
    
