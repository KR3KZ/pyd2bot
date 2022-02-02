from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem


@dataclass
class ForgettableSpellItem(SpellItem):
    available:bool
    
    
    def __post_init__(self):
        super().__init__()
    