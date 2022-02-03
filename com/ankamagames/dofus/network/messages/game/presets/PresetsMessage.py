from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.presets.Preset import Preset
    


class PresetsMessage(NetworkMessage):
    presets:list['Preset']
    

    def init(self, presets:list['Preset']):
        self.presets = presets
        
        super().__init__()
    
    