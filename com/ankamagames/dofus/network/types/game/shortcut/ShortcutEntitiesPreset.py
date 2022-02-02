from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


@dataclass
class ShortcutEntitiesPreset(Shortcut):
    presetId:int
    
    
    def __post_init__(self):
        super().__init__()
    