from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorMovement import TaxCollectorMovement


class TaxCollectorMovementsOfflineMessage(NetworkMessage):
    movements:list[TaxCollectorMovement]
    
    
