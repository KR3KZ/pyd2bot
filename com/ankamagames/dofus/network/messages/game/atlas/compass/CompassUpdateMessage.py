from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates


class CompassUpdateMessage(NetworkMessage):
    type:int
    coords:MapCoordinates
    
    
