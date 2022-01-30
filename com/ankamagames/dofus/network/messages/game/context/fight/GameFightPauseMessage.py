from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightPauseMessage(INetworkMessage):
    protocolId = 8818
    isPaused:bool
    
    
