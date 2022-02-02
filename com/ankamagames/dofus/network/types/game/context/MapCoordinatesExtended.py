from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.MapCoordinatesAndId import MapCoordinatesAndId


@dataclass
class MapCoordinatesExtended(MapCoordinatesAndId):
    subAreaId:int
    
    
    def __post_init__(self):
        super().__init__()
    