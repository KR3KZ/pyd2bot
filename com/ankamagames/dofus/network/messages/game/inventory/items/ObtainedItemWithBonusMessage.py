from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.items.ObtainedItemMessage import ObtainedItemMessage


@dataclass
class ObtainedItemWithBonusMessage(ObtainedItemMessage):
    bonusQuantity:int
    
    
    def __post_init__(self):
        super().__init__()
    