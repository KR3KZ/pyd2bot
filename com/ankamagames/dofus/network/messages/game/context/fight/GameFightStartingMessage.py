from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightStartingMessage(INetworkMessage):
    protocolId = 2951
    fightType:int
    fightId:int
    attackerId:int
    defenderId:int
    containsBoss:bool
    
    
