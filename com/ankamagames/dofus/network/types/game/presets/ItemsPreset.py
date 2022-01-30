from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook


class ItemsPreset(Preset):
    protocolId = 5400
    items:list[ItemForPreset]
    mountEquipped:bool
    look:EntityLook
    
