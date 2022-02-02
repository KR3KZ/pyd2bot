from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorMovement import TaxCollectorMovement


@dataclass
class TaxCollectorMovementsOfflineMessage(NetworkMessage):
    movements:list[TaxCollectorMovement]
    
    
    def __post_init__(self):
        super().__init__()
    