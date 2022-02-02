from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle


@dataclass
class MapObstacleUpdateMessage(NetworkMessage):
    obstacles:list[MapObstacle]
    
    
    def __post_init__(self):
        super().__init__()
    