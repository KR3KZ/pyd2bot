from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations
    


class AbstractTaxCollectorListMessage(NetworkMessage):
    informations:list['TaxCollectorInformations']
    

    def init(self, informations:list['TaxCollectorInformations']):
        self.informations = informations
        
        super().__init__()
    
    