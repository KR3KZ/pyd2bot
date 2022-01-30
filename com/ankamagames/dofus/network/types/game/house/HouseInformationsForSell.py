from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseInformationsForSell(NetworkMessage):
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
    
