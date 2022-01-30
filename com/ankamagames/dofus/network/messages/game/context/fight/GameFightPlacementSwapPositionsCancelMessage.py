from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightPlacementSwapPositionsCancelMessage(INetworkMessage):
    protocolId = 7054
    requestId:int
    
    
