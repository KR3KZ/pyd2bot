from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SpellItem import SpellItem


@dataclass
class SpellListMessage(NetworkMessage):
    spellPrevisualization:bool
    spells:list[SpellItem]
    
    
    def __post_init__(self):
        super().__init__()
    