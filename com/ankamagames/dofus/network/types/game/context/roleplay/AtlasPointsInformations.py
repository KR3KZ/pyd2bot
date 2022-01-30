from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended


class AtlasPointsInformations(NetworkMessage):
    protocolId = 4410
    type:int
    coords:MapCoordinatesExtended
    
    
