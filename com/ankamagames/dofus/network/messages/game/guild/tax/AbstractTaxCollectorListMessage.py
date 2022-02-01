from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations


class AbstractTaxCollectorListMessage(NetworkMessage):
    informations:list[TaxCollectorInformations]
    
    
