from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject


@dataclass
class ShortcutObjectIdolsPreset(ShortcutObject):
    presetId:int
    
    
    def __post_init__(self):
        super().__init__()
    