from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class GuildJoinedMessage(NetworkMessage):
    guildInfo:'GuildInformations'
    memberRights:int
    

    def init(self, guildInfo_:'GuildInformations', memberRights_:int):
        self.guildInfo = guildInfo_
        self.memberRights = memberRights_
        
        super().__init__()
    
    