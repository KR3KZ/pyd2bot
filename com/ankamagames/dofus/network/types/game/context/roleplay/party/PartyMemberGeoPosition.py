from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PartyMemberGeoPosition(NetworkMessage):
    protocolId = 6723
    memberId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
    
