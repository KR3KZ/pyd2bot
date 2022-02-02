from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


@dataclass
class ItemsPreset(Preset):
    items:list[ItemForPreset]
    mountEquipped:bool
    look:EntityLook
    
    
    def __post_init__(self):
        super().__init__()
    