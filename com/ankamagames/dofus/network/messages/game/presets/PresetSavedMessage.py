from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


@dataclass
class PresetSavedMessage(NetworkMessage):
    presetId:int
    preset:Preset
    
    
    def __post_init__(self):
        super().__init__()
    