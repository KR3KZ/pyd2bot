from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnListMessage(NetworkMessage):
    protocolId = 7238
    ids:list[float]
    deadsIds:list[float]
    
