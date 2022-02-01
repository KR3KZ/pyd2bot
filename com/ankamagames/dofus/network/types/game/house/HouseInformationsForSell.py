from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseInformationsForSell(INetworkMessage):
    protocolId = 1011
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
    skillListIds:int
    isLocked:bool
    price:int
    
    
