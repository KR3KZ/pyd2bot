from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended


class AtlasPointsInformations(NetworkMessage):
    type:int
    coords:list[MapCoordinatesExtended]
    
    
