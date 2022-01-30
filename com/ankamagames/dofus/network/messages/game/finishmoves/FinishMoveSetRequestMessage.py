from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FinishMoveSetRequestMessage(NetworkMessage):
    protocolId = 2738
    finishMoveId:int
    finishMoveState:bool
    
