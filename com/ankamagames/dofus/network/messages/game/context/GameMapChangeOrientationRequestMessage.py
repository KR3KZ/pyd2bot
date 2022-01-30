from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameMapChangeOrientationRequestMessage(INetworkMessage):
    protocolId = 4770
    direction:int
    
    
