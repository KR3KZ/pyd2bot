from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.Item import Item


@dataclass
class SpellItem(Item):
    spellId:int
    spellLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    