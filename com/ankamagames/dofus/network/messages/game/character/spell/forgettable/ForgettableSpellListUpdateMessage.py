from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ForgettableSpellItem import ForgettableSpellItem


@dataclass
class ForgettableSpellListUpdateMessage(NetworkMessage):
    action:int
    spells:list[ForgettableSpellItem]
    
    
    def __post_init__(self):
        super().__init__()
    