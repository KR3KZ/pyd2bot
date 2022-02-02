from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.social.GuildVersatileInformations import GuildVersatileInformations


@dataclass
class GuildVersatileInfoListMessage(NetworkMessage):
    guilds:list[GuildVersatileInformations]
    
    
    def __post_init__(self):
        super().__init__()
    