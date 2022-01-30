from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorMovement import TaxCollectorMovement


class TaxCollectorMovementsOfflineMessage(INetworkMessage):
    protocolId = 3016
    movements:TaxCollectorMovement
    
    
