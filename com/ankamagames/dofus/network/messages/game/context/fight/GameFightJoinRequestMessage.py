from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightJoinRequestMessage(INetworkMessage):
    protocolId = 6519
    fighterId:int
    fightId:int
    
    
