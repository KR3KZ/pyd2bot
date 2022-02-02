from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.presets.ItemForPreset import ItemForPreset


@dataclass
class ItemForPresetUpdateMessage(NetworkMessage):
    presetId:int
    presetItem:ItemForPreset
    
    
    def __post_init__(self):
        super().__init__()
    