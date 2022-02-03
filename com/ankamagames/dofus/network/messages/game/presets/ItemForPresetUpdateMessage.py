from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset
    


class ItemForPresetUpdateMessage(NetworkMessage):
    presetId:int
    presetItem:'ItemForPreset'
    

    def init(self, presetId:int, presetItem:'ItemForPreset'):
        self.presetId = presetId
        self.presetItem = presetItem
        
        super().__init__()
    
    