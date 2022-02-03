from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.BasicGuildInformations import BasicGuildInformations
    


class GuildInvitedMessage(NetworkMessage):
    recruterId:int
    recruterName:str
    guildInfo:'BasicGuildInformations'
    

    def init(self, recruterId:int, recruterName:str, guildInfo:'BasicGuildInformations'):
        self.recruterId = recruterId
        self.recruterName = recruterName
        self.guildInfo = guildInfo
        
        super().__init__()
    
    