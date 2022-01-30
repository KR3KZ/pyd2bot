from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameMapMovementCancelMessage(NetworkMessage):
    protocolId = 4409
    cellId:int
    
