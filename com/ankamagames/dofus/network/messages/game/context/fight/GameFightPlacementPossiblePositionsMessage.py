from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightPlacementPossiblePositionsMessage(INetworkMessage):
    protocolId = 3019
    positionsForChallengers:int
    positionsForDefenders:int
    teamNumber:int
    
    
