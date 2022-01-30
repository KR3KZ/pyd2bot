from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnFinishMessage(NetworkMessage):
    protocolId = 6692
    isAfk:bool
    
