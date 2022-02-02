from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.presets.IconPresetSaveRequestMessage import IconPresetSaveRequestMessage


@dataclass
class IdolsPresetSaveRequestMessage(IconPresetSaveRequestMessage):
    
    
    def __post_init__(self):
        super().__init__()
    