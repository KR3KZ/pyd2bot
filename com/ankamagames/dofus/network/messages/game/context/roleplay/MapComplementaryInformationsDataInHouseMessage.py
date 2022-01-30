from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsInside import HouseInformationsInside


class MapComplementaryInformationsDataInHouseMessage(MapComplementaryInformationsDataMessage):
    protocolId = 2024
    currentHouse:HouseInformationsInside
    
