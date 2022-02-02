from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.guild.GuildJoinedMessage import GuildJoinedMessage


@dataclass
class GuildMembershipMessage(GuildJoinedMessage):
    
    
    def __post_init__(self):
        super().__init__()
    