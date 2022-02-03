from com.ankamagames.dofus.network.messages.game.interactive.zaap.TeleportDestinationsMessage import TeleportDestinationsMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination
    


class ZaapDestinationsMessage(TeleportDestinationsMessage):
    spawnMapId:int
    

    def init(self, spawnMapId:int, type:int, destinations:list['TeleportDestination']):
        self.spawnMapId = spawnMapId
        
        super().__init__(type, destinations)
    
    