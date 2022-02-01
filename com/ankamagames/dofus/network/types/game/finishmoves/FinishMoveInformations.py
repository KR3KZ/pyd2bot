from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class FinishMoveInformations(INetworkMessage):
    protocolId = 2972
    finishMoveId:int
    finishMoveState:bool
    
    
