from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class ItemForPreset(NetworkMessage):
    position:int
    objGid:int
    objUid:int
    
    
    def __post_init__(self):
        super().__init__()
    