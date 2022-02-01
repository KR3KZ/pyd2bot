from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates


class CompassUpdateMessage(INetworkMessage):
    protocolId = 8716
    type:int
    coords:MapCoordinates
    
    
