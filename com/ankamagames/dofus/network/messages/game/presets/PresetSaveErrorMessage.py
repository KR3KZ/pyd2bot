from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class PresetSaveErrorMessage(NetworkMessage):
    presetId:int
    code:int
    
    
    def __post_init__(self):
        super().__init__()
    