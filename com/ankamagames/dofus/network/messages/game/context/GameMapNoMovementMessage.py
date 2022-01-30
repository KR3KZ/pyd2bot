from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameMapNoMovementMessage(NetworkMessage):
    protocolId = 8791
    cellX:int
    cellY:int
    
    
