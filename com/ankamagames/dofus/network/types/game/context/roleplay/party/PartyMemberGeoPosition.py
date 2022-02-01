from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PartyMemberGeoPosition(NetworkMessage):
    memberId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
    
