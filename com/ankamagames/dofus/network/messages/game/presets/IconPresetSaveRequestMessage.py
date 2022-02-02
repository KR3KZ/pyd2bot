from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


@dataclass
class IconPresetSaveRequestMessage(NetworkMessage):
    presetId:int
    symbolId:int
    updateData:bool
    
    
    def __post_init__(self):
        super().__init__()
    