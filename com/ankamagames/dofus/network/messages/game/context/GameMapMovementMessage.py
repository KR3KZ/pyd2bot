from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapMovementMessage(NetworkMessage):
    keyMovements:list[int]
    forcedDirection:int
    actorId:int
    
    
