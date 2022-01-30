from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPauseMessage(NetworkMessage):
    protocolId = 8818
    isPaused:bool
    
    
