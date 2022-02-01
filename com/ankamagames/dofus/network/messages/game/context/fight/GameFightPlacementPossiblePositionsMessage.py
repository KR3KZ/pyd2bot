from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightPlacementPossiblePositionsMessage(INetworkMessage):
    protocolId = 3019
    positionsForChallengers:int
    positionsForDefenders:int
    teamNumber:int
    
    
