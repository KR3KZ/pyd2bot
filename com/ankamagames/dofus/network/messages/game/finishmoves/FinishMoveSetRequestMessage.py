from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FinishMoveSetRequestMessage(NetworkMessage):
    finishMoveId:int
    finishMoveState:bool
    

    def init(self, finishMoveId:int, finishMoveState:bool):
        self.finishMoveId = finishMoveId
        self.finishMoveState = finishMoveState
        
        super().__init__()
    
    