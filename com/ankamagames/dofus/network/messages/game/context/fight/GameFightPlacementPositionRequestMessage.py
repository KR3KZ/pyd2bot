from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameFightPlacementPositionRequestMessage(INetworkMessage):
    protocolId = 5499
    cellId:int
    
    
