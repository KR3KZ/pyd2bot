from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    


class ItemsPreset(Preset):
    items:list['ItemForPreset']
    mountEquipped:bool
    look:'EntityLook'
    

    def init(self, items:list['ItemForPreset'], mountEquipped:bool, look:'EntityLook', id:int):
        self.items = items
        self.mountEquipped = mountEquipped
        self.look = look
        
        super().__init__(id)
    
    