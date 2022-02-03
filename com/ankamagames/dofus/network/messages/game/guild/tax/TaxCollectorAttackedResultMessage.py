from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.guild.tax.TaxCollectorBasicInformations import TaxCollectorBasicInformations
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class TaxCollectorAttackedResultMessage(NetworkMessage):
    deadOrAlive:bool
    basicInfos:'TaxCollectorBasicInformations'
    guild:'BasicGuildInformations'
    

    def init(self, deadOrAlive:bool, basicInfos:'TaxCollectorBasicInformations', guild:'BasicGuildInformations'):
        self.deadOrAlive = deadOrAlive
        self.basicInfos = basicInfos
        self.guild = guild
        
        super().__init__()
    
    