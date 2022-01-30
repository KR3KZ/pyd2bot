from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(NetworkMessage):
    protocolId = 519
    requestId:int
    requesterId:int
    requesterCellId:int
    requestedId:int
    requestedCellId:int
    
    
