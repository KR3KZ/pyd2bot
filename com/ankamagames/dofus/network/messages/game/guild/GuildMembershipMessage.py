from com.ankamagames.dofus.network.messages.game.guild.GuildJoinedMessage import GuildJoinedMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    


class GuildMembershipMessage(GuildJoinedMessage):
    

    def init(self, guildInfo:'GuildInformations', memberRights:int):
        
        super().__init__(guildInfo, memberRights)
    
    