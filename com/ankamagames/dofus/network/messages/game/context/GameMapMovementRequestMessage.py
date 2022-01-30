from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameMapMovementRequestMessage(INetworkMessage):
    protocolId = 685
    keyMovements:int
    mapId:int
    
    
