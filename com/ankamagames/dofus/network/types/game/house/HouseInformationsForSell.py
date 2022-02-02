from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


@dataclass
class HouseInformationsForSell(NetworkMessage):
    instanceId:int
    secondHand:bool
    modelId:int
    ownerTag:AccountTagInformation
    hasOwner:bool
    ownerCharacterName:str
    worldX:int
    worldY:int
    subAreaId:int
    nbRoom:int
    nbChest:int
    skillListIds:list[int]
    isLocked:bool
    price:int
    
    
    def __post_init__(self):
        super().__init__()
    