from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates


class MapCoordinatesAndId(MapCoordinates):
    mapId:int
    

    def init(self, mapId:int, worldX:int, worldY:int):
        self.mapId = mapId
        
        super().__init__(worldX, worldY)
    
    