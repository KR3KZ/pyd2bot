from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.shortcut.ShortcutObject import ShortcutObject


@dataclass
class ShortcutObjectPreset(ShortcutObject):
    presetId:int
    
    
    def __post_init__(self):
        super().__init__()
    