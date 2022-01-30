from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameFightPlacementSwapPositionsCancelMessage(NetworkMessage):
    protocolId = 7054
    requestId:int
    
