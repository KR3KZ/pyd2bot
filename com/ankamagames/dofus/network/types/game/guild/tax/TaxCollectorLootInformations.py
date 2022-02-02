from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations


@dataclass
class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
    kamas:int
    experience:int
    pods:int
    itemsValue:int
    
    
    def __post_init__(self):
        super().__init__()
    