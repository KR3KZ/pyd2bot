from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameMapSpeedMovementMessage(NetworkMessage):
    protocolId = 8414
    speedMultiplier:int
    
