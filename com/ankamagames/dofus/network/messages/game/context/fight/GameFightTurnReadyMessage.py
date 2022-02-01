from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightTurnReadyMessage(INetworkMessage):
    protocolId = 4043
    isReady:bool
    
    
