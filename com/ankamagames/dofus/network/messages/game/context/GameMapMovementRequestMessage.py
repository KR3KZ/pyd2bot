from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameMapMovementRequestMessage(NetworkMessage):
    protocolId = 685
    keyMovements:list[int]
    mapId:float
    
