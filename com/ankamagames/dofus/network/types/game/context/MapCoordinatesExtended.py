from com.ankamagames.dofus.network.types.game.context.MapCoordinatesAndId import MapCoordinatesAndId


class MapCoordinatesExtended(MapCoordinatesAndId):
    subAreaId:int
    

    def init(self, subAreaId:int, mapId:int, worldX:int, worldY:int):
        self.subAreaId = subAreaId
        
        super().__init__(mapId, worldX, worldY)
    
    