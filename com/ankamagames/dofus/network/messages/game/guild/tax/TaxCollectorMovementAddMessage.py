from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorInformations import TaxCollectorInformations


class TaxCollectorMovementAddMessage(INetworkMessage):
    protocolId = 6509
    informations:TaxCollectorInformations
    
    
