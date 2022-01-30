from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    protocolId = 519
    requestId:int
    requesterId:float
    requesterCellId:int
    requestedId:float
    requestedCellId:int
    
