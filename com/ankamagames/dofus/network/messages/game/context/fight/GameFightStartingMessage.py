from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightStartingMessage(NetworkMessage):
    fightType:int
    fightId:int
    attackerId:int
    defenderId:int
    containsBoss:bool
    
    
