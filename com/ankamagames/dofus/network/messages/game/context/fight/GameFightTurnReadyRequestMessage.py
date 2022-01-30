from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnReadyRequestMessage(NetworkMessage):
    protocolId = 4389
    id:int
    
    
