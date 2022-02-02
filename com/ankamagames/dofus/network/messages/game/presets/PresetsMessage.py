from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.Preset import Preset


@dataclass
class PresetsMessage(NetworkMessage):
    presets:list[Preset]
    
    
    def __post_init__(self):
        super().__init__()
    