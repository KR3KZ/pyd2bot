from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


@dataclass
class EntitiesPreset(Preset):
    iconId:int
    entityIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    