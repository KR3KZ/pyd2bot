from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


@dataclass
class ShortcutBarContentMessage(NetworkMessage):
    barType:int
    shortcuts:list[Shortcut]
    
    
    def __post_init__(self):
        super().__init__()
    