from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementPossiblePositionsMessage(NetworkMessage):
    protocolId = 3019
    positionsForChallengers:list[int]
    positionsForDefenders:list[int]
    teamNumber:int
    
