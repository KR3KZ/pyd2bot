from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


class AccountHouseInformations(HouseInformations):
    protocolId = 3170
    houseInfos:HouseInstanceInformations
    worldX:int
    worldY:int
    mapId:int
    subAreaId:int
    
