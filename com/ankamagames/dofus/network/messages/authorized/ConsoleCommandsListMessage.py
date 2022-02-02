from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ConsoleCommandsListMessage(NetworkMessage):
    aliases:list[str]
    args:list[str]
    descriptions:list[str]
    
    
    def __post_init__(self):
        super().__init__()
    