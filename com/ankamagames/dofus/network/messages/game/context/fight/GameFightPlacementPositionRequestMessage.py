from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameFightPlacementPositionRequestMessage(INetworkMessage):
    protocolId = 5499
    cellId:int
    
    
