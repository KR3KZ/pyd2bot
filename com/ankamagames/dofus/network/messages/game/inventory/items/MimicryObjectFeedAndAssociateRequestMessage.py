from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectAssociateRequestMessage import SymbioticObjectAssociateRequestMessage


@dataclass
class MimicryObjectFeedAndAssociateRequestMessage(SymbioticObjectAssociateRequestMessage):
    foodUID:int
    foodPos:int
    preview:bool
    
    
    def __post_init__(self):
        super().__init__()
    