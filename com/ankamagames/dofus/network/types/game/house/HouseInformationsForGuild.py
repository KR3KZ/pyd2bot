from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation


class HouseInformationsForGuild(HouseInformations):
    protocolId = 3219
    instanceId:int
    secondHand:bool
    ownerTag:AccountTagInformation
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    skillListIds:int
    guildshareParams:int
    
    
