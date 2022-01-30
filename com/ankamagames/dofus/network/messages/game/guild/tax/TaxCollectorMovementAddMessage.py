from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations


class TaxCollectorMovementAddMessage(NetworkMessage):
    protocolId = 6509
    informations:TaxCollectorInformations
    
    
