from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.presets.PresetUseResultMessage import PresetUseResultMessage


@dataclass
class PresetUseResultWithMissingIdsMessage(PresetUseResultMessage):
    missingIds:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    