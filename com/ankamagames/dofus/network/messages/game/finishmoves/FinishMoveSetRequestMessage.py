from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FinishMoveSetRequestMessage(INetworkMessage):
    protocolId = 2738
    finishMoveId:int
    finishMoveState:bool
    
    
