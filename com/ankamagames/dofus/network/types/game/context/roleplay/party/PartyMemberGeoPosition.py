from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PartyMemberGeoPosition(INetworkMessage):
    protocolId = 6723
    memberId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
    
