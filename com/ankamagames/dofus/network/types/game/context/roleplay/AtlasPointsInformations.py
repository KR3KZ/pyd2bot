from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.MapCoordinatesExtended import MapCoordinatesExtended
    


class AtlasPointsInformations(NetworkMessage):
    type:int
    coords:list['MapCoordinatesExtended']
    

    def init(self, type:int, coords:list['MapCoordinatesExtended']):
        self.type = type
        self.coords = coords
        
        super().__init__()
    
    