from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class AllianceGuildLeavingMessage(NetworkMessage):
    kicked:bool
    guildId:int
    
    
    def __post_init__(self):
        super().__init__()
    