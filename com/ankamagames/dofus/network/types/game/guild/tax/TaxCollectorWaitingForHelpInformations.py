from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo


@dataclass
class TaxCollectorWaitingForHelpInformations(TaxCollectorComplementaryInformations):
    waitingForHelpInfo:ProtectedEntityWaitingForHelpInfo
    
    
    def __post_init__(self):
        super().__init__()
    