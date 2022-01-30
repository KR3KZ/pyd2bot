from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameMapNoMovementMessage(INetworkMessage):
    protocolId = 8791
    cellX:int
    cellY:int
    
    
