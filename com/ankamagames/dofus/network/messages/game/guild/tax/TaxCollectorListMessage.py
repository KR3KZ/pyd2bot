from com.ankamagames.dofus.network.messages.game.guild.tax.AbstractTaxCollectorListMessage import AbstractTaxCollectorListMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorFightersInformation import TaxCollectorFightersInformation
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations
    


class TaxCollectorListMessage(AbstractTaxCollectorListMessage):
    nbcollectorMax:int
    fightersInformations:list['TaxCollectorFightersInformation']
    infoType:int
    

    def init(self, nbcollectorMax:int, fightersInformations:list['TaxCollectorFightersInformation'], infoType:int, informations:list['TaxCollectorInformations']):
        self.nbcollectorMax = nbcollectorMax
        self.fightersInformations = fightersInformations
        self.infoType = infoType
        
        super().__init__(informations)
    
    