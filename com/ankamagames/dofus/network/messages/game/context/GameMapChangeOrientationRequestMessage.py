from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameMapChangeOrientationRequestMessage(NetworkMessage):
    protocolId = 4770
    direction:int
    
    
