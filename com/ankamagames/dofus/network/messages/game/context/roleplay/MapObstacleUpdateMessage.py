from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.MapObstacle import MapObstacle


class MapObstacleUpdateMessage(NetworkMessage):
    protocolId = 9984
    obstacles:list[MapObstacle]
    
