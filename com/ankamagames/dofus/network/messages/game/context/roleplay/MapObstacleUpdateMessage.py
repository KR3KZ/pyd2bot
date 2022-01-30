from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle


class MapObstacleUpdateMessage(INetworkMessage):
    protocolId = 9984
    obstacles:MapObstacle
    
    
