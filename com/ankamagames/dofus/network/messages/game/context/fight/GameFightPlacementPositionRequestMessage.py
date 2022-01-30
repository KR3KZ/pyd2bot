from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementPositionRequestMessage(NetworkMessage):
    protocolId = 5499
    cellId:int
    
