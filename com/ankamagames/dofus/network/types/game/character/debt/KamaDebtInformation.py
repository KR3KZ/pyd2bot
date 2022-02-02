from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.character.debt.DebtInformation import DebtInformation


@dataclass
class KamaDebtInformation(DebtInformation):
    kamas:int
    
    
    def __post_init__(self):
        super().__init__()
    