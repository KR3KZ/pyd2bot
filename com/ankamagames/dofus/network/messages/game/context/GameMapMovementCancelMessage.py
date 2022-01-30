from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameMapMovementCancelMessage(INetworkMessage):
    protocolId = 4409
    cellId:int
    
    
