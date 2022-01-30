from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightStartingMessage(NetworkMessage):
    protocolId = 2951
    fightType:int
    fightId:int
    attackerId:float
    defenderId:float
    containsBoss:bool
    
