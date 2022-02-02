from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class GuildEmblem(NetworkMessage):
    symbolShape:int
    symbolColor:int
    backgroundShape:int
    backgroundColor:int
    
    
    def __post_init__(self):
        super().__init__()
    