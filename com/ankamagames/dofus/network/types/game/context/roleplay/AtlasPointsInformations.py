from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended


class AtlasPointsInformations(INetworkMessage):
    protocolId = 4410
    type:int
    coords:MapCoordinatesExtended
    
    
