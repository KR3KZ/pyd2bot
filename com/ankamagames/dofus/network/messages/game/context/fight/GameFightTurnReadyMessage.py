from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnReadyMessage(NetworkMessage):
    protocolId = 4043
    isReady:bool
    
    
