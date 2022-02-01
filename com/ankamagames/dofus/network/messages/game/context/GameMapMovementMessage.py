from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameMapMovementMessage(INetworkMessage):
    protocolId = 1972
    keyMovements:int
    forcedDirection:int
    actorId:int
    
    
