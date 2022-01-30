from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsCancelledMessage(NetworkMessage):
    protocolId = 998
    requestId:int
    cancellerId:int
    
