from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.interactive.zaap.TeleportDestinationsMessage import TeleportDestinationsMessage


@dataclass
class ZaapDestinationsMessage(TeleportDestinationsMessage):
    spawnMapId:int
    
    
    def __post_init__(self):
        super().__init__()
    