from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameFightPlacementPossiblePositionsMessage(NetworkMessage):
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    teamNumber:int
    
    
