from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from com.ankamagames.dofus.network.types.game.fight.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo


class TaxCollectorWaitingForHelpInformations(TaxCollectorComplementaryInformations):
    protocolId = 3199
    waitingForHelpInfo:ProtectedEntityWaitingForHelpInfo
    
