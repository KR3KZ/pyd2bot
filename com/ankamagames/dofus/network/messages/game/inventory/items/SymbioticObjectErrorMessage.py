from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.items.ObjectErrorMessage import ObjectErrorMessage


@dataclass
class SymbioticObjectErrorMessage(ObjectErrorMessage):
    errorCode:int
    
    
    def __post_init__(self):
        super().__init__()
    