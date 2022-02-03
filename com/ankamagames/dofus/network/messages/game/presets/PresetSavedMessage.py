from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
    


class PresetSavedMessage(NetworkMessage):
    presetId:int
    preset:'Preset'
    

    def init(self, presetId:int, preset:'Preset'):
        self.presetId = presetId
        self.preset = preset
        
        super().__init__()
    
    