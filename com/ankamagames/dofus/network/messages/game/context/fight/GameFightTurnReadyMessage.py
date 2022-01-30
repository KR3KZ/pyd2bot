from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightTurnReadyMessage(INetworkMessage):
    protocolId = 4043
    isReady:bool
    
    
