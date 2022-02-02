from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.interactive.zaap.TeleportDestination import TeleportDestination


@dataclass
class TeleportDestinationsMessage(NetworkMessage):
    type:int
    destinations:list[TeleportDestination]
    
    
    def __post_init__(self):
        super().__init__()
    