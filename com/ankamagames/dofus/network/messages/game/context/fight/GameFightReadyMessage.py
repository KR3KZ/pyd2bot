from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightReadyMessage(NetworkMessage):
    protocolId = 3480
    isReady:bool
    
