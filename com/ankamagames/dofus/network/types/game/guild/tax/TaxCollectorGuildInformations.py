from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


@dataclass
class TaxCollectorGuildInformations(TaxCollectorComplementaryInformations):
    guild:BasicGuildInformations
    
    
    def __post_init__(self):
        super().__init__()
    