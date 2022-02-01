from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightPlacementSwapPositionsCancelMessage(INetworkMessage):
    protocolId = 7054
    requestId:int
    
    
