from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsCancelledMessage(NetworkMessage):
    requestId:int
    cancellerId:int
    
    
