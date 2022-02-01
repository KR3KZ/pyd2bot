from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightPauseMessage(INetworkMessage):
    protocolId = 8818
    isPaused:bool
    
    
