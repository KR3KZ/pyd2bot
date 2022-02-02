from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations


@dataclass
class AbstractTaxCollectorListMessage(NetworkMessage):
    informations:list[TaxCollectorInformations]
    
    
    def __post_init__(self):
        super().__init__()
    