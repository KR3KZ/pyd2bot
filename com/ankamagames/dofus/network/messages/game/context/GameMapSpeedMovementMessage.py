from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameMapSpeedMovementMessage(INetworkMessage):
    protocolId = 8414
    speedMultiplier:int
    
    
