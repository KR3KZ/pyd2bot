from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightTurnFinishMessage(INetworkMessage):
    protocolId = 6692
    isAfk:bool
    
    
