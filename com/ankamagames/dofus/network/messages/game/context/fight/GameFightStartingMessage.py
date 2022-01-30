from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightStartingMessage(NetworkMessage):
    protocolId = 2951
    fightType:int
    fightId:int
    attackerId:int
    defenderId:int
    containsBoss:bool
    
    
