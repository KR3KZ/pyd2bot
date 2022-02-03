from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseInstanceInformations(NetworkMessage):
    instanceId:int
    ownerTag:'AccountTagInformation'
    price:int
    secondHand:bool
    isLocked:bool
    hasOwner:bool
    isSaleLocked:bool
    

    def init(self, instanceId:int, ownerTag:'AccountTagInformation', price:int):
        self.instanceId = instanceId
        self.ownerTag = ownerTag
        self.price = price
        
        super().__init__()
    
    