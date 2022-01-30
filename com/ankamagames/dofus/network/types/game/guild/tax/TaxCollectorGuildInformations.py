from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations


class TaxCollectorGuildInformations(TaxCollectorComplementaryInformations):
    protocolId = 2529
    guild:BasicGuildInformations
    
    
