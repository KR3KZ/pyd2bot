from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.items.SymbioticObjectErrorMessage import SymbioticObjectErrorMessage


@dataclass
class MimicryObjectErrorMessage(SymbioticObjectErrorMessage):
    preview:bool
    
    
    def __post_init__(self):
        super().__init__()
    