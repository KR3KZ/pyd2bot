from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle


class MapObstacleUpdateMessage(NetworkMessage):
    obstacles:list[MapObstacle]
    
    
