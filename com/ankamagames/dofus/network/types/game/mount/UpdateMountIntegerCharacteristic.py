from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.mount.UpdateMountCharacteristic import UpdateMountCharacteristic


@dataclass
class UpdateMountIntegerCharacteristic(UpdateMountCharacteristic):
    value:int
    
    
    def __post_init__(self):
        super().__init__()
    