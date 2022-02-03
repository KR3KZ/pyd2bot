from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsCancelledMessage(NetworkMessage):
    requestId:int
    cancellerId:int
    

    def init(self, requestId:int, cancellerId:int):
        self.requestId = requestId
        self.cancellerId = cancellerId
        
        super().__init__()
    
    