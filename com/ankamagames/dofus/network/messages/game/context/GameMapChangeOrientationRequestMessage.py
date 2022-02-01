from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameMapChangeOrientationRequestMessage(INetworkMessage):
    protocolId = 4770
    direction:int
    
    
