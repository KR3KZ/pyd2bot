from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameMapMovementMessage(NetworkMessage):
    protocolId = 1972
    keyMovements:int
    forcedDirection:int
    actorId:int
    
