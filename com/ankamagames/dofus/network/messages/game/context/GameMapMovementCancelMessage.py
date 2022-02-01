from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameMapMovementCancelMessage(INetworkMessage):
    protocolId = 4409
    cellId:int
    
    
