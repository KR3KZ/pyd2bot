from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorFightersInformation import TaxCollectorFightersInformation


class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
    protocolId = 4811
    nbcollectorMax:int
    fightersInformations:TaxCollectorFightersInformation
    infoType:int
    
