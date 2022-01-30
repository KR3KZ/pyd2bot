from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightPlacementSwapPositionsOfferMessage(INetworkMessage):
    protocolId = 519
    requestId:int
    requesterId:int
    requesterCellId:int
    requestedId:int
    requestedCellId:int
    
    
