from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates


@dataclass
class CompassUpdateMessage(NetworkMessage):
    type:int
    coords:MapCoordinates
    
    
    def __post_init__(self):
        super().__init__()
    