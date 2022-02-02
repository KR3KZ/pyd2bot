from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.guild.GuildMember import GuildMember


@dataclass
class GuildInformationsMemberUpdateMessage(NetworkMessage):
    member:GuildMember
    
    
    def __post_init__(self):
        super().__init__()
    