from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


@dataclass
class HouseInformationsForGuild(HouseInformations):
    instanceId:int
    secondHand:bool
    ownerTag:AccountTagInformation
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    skillListIds:list[int]
    guildshareParams:int
    
    
    def __post_init__(self):
        super().__init__()
    