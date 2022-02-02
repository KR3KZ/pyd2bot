from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorFightersInformation import TaxCollectorFightersInformation


@dataclass
class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
    nbcollectorMax:int
    fightersInformations:list[TaxCollectorFightersInformation]
    infoType:int
    
    
    def __post_init__(self):
        super().__init__()
    