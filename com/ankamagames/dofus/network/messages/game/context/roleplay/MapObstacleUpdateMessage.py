from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle
    


class MapObstacleUpdateMessage(NetworkMessage):
    obstacles:list['MapObstacle']
    

    def init(self, obstacles:list['MapObstacle']):
        self.obstacles = obstacles
        
        super().__init__()
    
    