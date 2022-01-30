from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations


class AbstractTaxCollectorListMessage(NetworkMessage):
    protocolId = 6496
    informations:list[TaxCollectorInformations]
    
