from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.PresetsContainerPreset import PresetsContainerPreset


@dataclass
class IconNamedPreset(PresetsContainerPreset):
    iconId:int
    name:str
    
    
    def __post_init__(self):
        super().__init__()
    