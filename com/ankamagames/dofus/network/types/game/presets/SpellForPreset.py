from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class SpellForPreset(NetworkMessage):
    spellId:int
    shortcuts:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    