from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightPlacementSwapPositionsCancelledMessage(INetworkMessage):
    protocolId = 998
    requestId:int
    cancellerId:int
    
    
