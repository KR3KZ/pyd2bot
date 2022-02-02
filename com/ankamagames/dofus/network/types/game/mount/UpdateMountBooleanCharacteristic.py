from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


@dataclass
class UpdateMountBooleanCharacteristic(UpdateMountCharacteristic):
    value:bool
    
    
    def __post_init__(self):
        super().__init__()
    