from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightPlacementSwapPositionsAcceptMessage(INetworkMessage):
    protocolId = 2140
    requestId:int
    
    
