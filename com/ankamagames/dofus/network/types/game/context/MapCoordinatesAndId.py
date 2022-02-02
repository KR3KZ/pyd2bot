from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates


@dataclass
class MapCoordinatesAndId(MapCoordinates):
    mapId:int
    
    
    def __post_init__(self):
        super().__init__()
    