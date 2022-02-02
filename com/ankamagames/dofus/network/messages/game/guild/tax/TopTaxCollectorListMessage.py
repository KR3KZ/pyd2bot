from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage


@dataclass
class TopTaxCollectorListMessage(AbstractTaxCollectorListMessage):
    isDungeon:bool
    
    
    def __post_init__(self):
        super().__init__()
    