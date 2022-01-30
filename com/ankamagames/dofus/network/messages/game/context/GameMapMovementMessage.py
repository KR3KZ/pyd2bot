from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameMapMovementMessage(NetworkMessage):
    protocolId = 1972
    keyMovements:list[int]
    forcedDirection:int
    actorId:float
    
