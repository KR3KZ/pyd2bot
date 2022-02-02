from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


@dataclass
class HouseInstanceInformations(NetworkMessage):
    instanceId:int
    ownerTag:AccountTagInformation
    price:int
    secondHand:bool
    isLocked:bool
    hasOwner:bool
    isSaleLocked:bool
    
    
    def __post_init__(self):
        super().__init__()
    