from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectUseMessage import ObjectUseMessage


@dataclass
class ObjectUseMultipleMessage(ObjectUseMessage):
    quantity:int
    
    
    def __post_init__(self):
        super().__init__()
    