from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnStartMessage(NetworkMessage):
    protocolId = 3772
    id:int
    waitTime:int
    
