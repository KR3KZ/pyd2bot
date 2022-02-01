from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    requestId:int
    requesterId:int
    requesterCellId:int
    requestedId:int
    requestedCellId:int
    
    
