from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class FinishMoveInformations(INetworkMessage):
    protocolId = 2972
    finishMoveId:int
    finishMoveState:bool
    
    
