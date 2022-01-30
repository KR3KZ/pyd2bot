from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorMovement import TaxCollectorMovement


class TaxCollectorMovementsOfflineMessage(NetworkMessage):
    protocolId = 3016
    movements:list[TaxCollectorMovement]
    
