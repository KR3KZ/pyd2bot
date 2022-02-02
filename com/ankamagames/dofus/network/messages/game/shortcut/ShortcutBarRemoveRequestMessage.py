from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ShortcutBarRemoveRequestMessage(NetworkMessage):
    barType:int
    slot:int
    
    
    def __post_init__(self):
        super().__init__()
    