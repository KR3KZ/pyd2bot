from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightReadyMessage(INetworkMessage):
    protocolId = 3480
    isReady:bool
    
    
