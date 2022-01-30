from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class FinishMoveInformations(NetworkMessage):
    protocolId = 2972
    finishMoveId:int
    finishMoveState:bool
    
    
