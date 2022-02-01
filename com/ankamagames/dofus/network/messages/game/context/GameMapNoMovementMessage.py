from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameMapNoMovementMessage(INetworkMessage):
    protocolId = 8791
    cellX:int
    cellY:int
    
    
