from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnEndMessage(NetworkMessage):
    protocolId = 4443
    id:float
    
