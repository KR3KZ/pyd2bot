from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MapCoordinates(NetworkMessage):
    protocolId = 3568
    worldX:int
    worldY:int
    
    
