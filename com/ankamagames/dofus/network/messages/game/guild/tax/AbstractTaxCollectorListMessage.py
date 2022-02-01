from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations


class AbstractTaxCollectorListMessage(INetworkMessage):
    protocolId = 6496
    informations:TaxCollectorInformations
    
    
