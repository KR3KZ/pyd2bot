from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightPlacementSwapPositionsCancelledMessage(INetworkMessage):
    protocolId = 998
    requestId:int
    cancellerId:int
    
    
