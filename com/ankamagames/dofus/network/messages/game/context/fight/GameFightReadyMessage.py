from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightReadyMessage(INetworkMessage):
    protocolId = 3480
    isReady:bool
    
    
