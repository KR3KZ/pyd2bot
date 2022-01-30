from com.ankamagames.dofus.network.types.game.house.HouseInformations import HouseInformations
from com.ankamagames.dofus.network.types.game.house.HouseInstanceInformations import HouseInstanceInformations


class HouseInformationsInside(HouseInformations):
    protocolId = 2517
    houseInfos:HouseInstanceInformations
    worldX:int
    worldY:int
    
