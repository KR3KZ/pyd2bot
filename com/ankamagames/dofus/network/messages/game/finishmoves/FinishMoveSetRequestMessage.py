from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FinishMoveSetRequestMessage(NetworkMessage):
    finishMoveId:int
    finishMoveState:bool
    
    
