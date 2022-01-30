from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinates import MapCoordinates


class CompassUpdateMessage(NetworkMessage):
    protocolId = 8716
    type:int
    coords:MapCoordinates
    
    
