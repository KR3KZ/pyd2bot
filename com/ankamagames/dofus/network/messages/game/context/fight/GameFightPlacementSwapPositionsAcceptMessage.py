from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsAcceptMessage(NetworkMessage):
    protocolId = 2140
    requestId:int
    
