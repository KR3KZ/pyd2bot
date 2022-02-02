from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GuildVersatileInformations(NetworkMessage):
    guildId:int
    leaderId:int
    guildLevel:int
    nbMembers:int
    
    
    def __post_init__(self):
        super().__init__()
    