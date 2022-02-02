from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations


@dataclass
class TaxCollectorMovementAddMessage(NetworkMessage):
    informations:TaxCollectorInformations
    
    
    def __post_init__(self):
        super().__init__()
    