from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FinishMoveSetRequestMessage(INetworkMessage):
    protocolId = 2738
    finishMoveId:int
    finishMoveState:bool
    
    
