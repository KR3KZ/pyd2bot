from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class TaxCollectorDialogQuestionBasicMessage(NetworkMessage):
    guildInfo:'BasicGuildInformations'
    

    def init(self, guildInfo:'BasicGuildInformations'):
        self.guildInfo = guildInfo
        
        super().__init__()
    
    