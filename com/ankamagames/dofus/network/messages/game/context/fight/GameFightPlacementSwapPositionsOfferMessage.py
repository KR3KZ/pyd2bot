from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    requestId:int
    requesterId:int
    requesterCellId:int
    requestedId:int
    requestedCellId:int
    

    def init(self, requestId:int, requesterId:int, requesterCellId:int, requestedId:int, requestedCellId:int):
        self.requestId = requestId
        self.requesterId = requesterId
        self.requesterCellId = requesterCellId
        self.requestedId = requestedId
        self.requestedCellId = requestedCellId
        
        super().__init__()
    
    