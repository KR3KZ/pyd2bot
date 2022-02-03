from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class HouseInformationsForGuild(HouseInformations):
    instanceId:int
    secondHand:bool
    ownerTag:'AccountTagInformation'
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    skillListIds:list[int]
    guildshareParams:int
    

    def init(self, instanceId:int, secondHand:bool, ownerTag:'AccountTagInformation', worldX:int, worldY:int, mapId:int, subAreaId:int, skillListIds:list[int], guildshareParams:int, houseId:int, modelId:int):
        self.instanceId = instanceId
        self.secondHand = secondHand
        self.ownerTag = ownerTag
        self.worldX = worldX
        self.worldY = worldY
        self.mapId = mapId
        self.subAreaId = subAreaId
        self.skillListIds = skillListIds
        self.guildshareParams = guildshareParams
        
        super().__init__(houseId, modelId)
    
    