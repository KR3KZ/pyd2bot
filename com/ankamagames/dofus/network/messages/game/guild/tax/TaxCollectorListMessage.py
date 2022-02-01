from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorFightersInformation import TaxCollectorFightersInformation


class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
    nbcollectorMax:int
    fightersInformations:list[TaxCollectorFightersInformation]
    infoType:int
    
    
