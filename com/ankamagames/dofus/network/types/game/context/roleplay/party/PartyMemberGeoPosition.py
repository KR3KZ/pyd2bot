from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PartyMemberGeoPosition(NetworkMessage):
    memberId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    

    def init(self, memberId:int, worldX:int, worldY:int, mapId:int, subAreaId:int):
        self.memberId = memberId
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        
        super().__init__()
    
    