from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseInstanceInformations(INetworkMessage):
    protocolId = 3243
    instanceId:int
    ownerTag:AccountTagInformation
    price:int
    secondHand:bool
    isLocked:bool
    hasOwner:bool
    isSaleLocked:bool
    
    
