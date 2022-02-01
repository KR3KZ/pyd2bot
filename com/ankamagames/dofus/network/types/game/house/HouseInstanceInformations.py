from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseInstanceInformations(NetworkMessage):
    instanceId:int
    ownerTag:AccountTagInformation
    price:int
    secondHand:bool
    isLocked:bool
    hasOwner:bool
    isSaleLocked:bool
    
    
