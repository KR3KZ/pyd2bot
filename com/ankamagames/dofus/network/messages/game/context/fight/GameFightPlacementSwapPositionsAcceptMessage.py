from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightPlacementSwapPositionsAcceptMessage(INetworkMessage):
    protocolId = 2140
    requestId:int
    
    
