from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameMapSpeedMovementMessage(INetworkMessage):
    protocolId = 8414
    speedMultiplier:int
    
    
