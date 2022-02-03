from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class GuildJoinedMessage(NetworkMessage):
    guildInfo:'GuildInformations'
    memberRights:int
    

    def init(self, guildInfo:'GuildInformations', memberRights:int):
        self.guildInfo = guildInfo
        self.memberRights = memberRights
        
        super().__init__()
    
    