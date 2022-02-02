from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended


@dataclass
class AtlasPointsInformations(NetworkMessage):
    type:int
    coords:list[MapCoordinatesExtended]
    
    
    def __post_init__(self):
        super().__init__()
    