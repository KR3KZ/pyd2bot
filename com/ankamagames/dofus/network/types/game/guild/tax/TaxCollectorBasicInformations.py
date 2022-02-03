from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TaxCollectorBasicInformations(NetworkMessage):
    firstNameId:int
    lastNameId:int
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    

    def init(self, firstNameId:int, lastNameId:int, worldX:int, worldY:int, mapId:int, subAreaId:int):
        self.firstNameId = firstNameId
        self.lastNameId = lastNameId
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        
        super().__init__()
    
    