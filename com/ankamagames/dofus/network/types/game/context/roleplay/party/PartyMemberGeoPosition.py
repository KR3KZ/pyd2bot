from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PartyMemberGeoPosition(INetworkMessage):
    protocolId = 6723
    memberId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
    
