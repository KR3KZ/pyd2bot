from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseInformationsForSell(NetworkMessage):
    instanceId:int
    secondHand:bool
    modelId:int
    ownerTag:'AccountTagInformation'
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
    

    def init(self, instanceId:int, secondHand:bool, modelId:int, ownerTag:'AccountTagInformation', hasOwner:bool, ownerCharacterName:str, worldX:int, worldY:int, subAreaId:int, nbRoom:int, nbChest:int, skillListIds:list[int], isLocked:bool, price:int):
        self.instanceId = instanceId
        self.secondHand = secondHand
        self.modelId = modelId
        self.ownerTag = ownerTag
        self.hasOwner = hasOwner
        self.ownerCharacterName = ownerCharacterName
        self.worldX = worldX
        self.worldY = worldY
        self.subAreaId = subAreaId
        self.nbRoom = nbRoom
        self.nbChest = nbChest
        self.skillListIds = skillListIds
        self.isLocked = isLocked
        self.price = price
        
        super().__init__()
    
    