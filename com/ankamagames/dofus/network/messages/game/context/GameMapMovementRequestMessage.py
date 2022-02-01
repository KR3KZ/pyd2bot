from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameMapMovementRequestMessage(NetworkMessage):
    keyMovements:list[int]
    mapId:int
    
    
