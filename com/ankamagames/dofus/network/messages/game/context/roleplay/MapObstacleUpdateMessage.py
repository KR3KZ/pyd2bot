from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle


class MapObstacleUpdateMessage(INetworkMessage):
    protocolId = 9984
    obstacles:MapObstacle
    
    
