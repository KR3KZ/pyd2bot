from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MapCoordinates(INetworkMessage):
    protocolId = 3568
    worldX:int
    worldY:int
    
    
