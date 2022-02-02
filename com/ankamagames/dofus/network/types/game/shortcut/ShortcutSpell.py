from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.shortcut.Shortcut import Shortcut


@dataclass
class ShortcutSpell(Shortcut):
    spellId:int
    
    
    def __post_init__(self):
        super().__init__()
    