from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject


@dataclass
class ShortcutObjectItem(ShortcutObject):
    itemUID:int
    itemGID:int
    
    
    def __post_init__(self):
        super().__init__()
    