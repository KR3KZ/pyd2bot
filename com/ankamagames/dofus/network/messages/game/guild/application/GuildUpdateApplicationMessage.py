from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GuildUpdateApplicationMessage(NetworkMessage):
    applyText:str
    guildId:int
    
    
    def __post_init__(self):
        super().__init__()
    