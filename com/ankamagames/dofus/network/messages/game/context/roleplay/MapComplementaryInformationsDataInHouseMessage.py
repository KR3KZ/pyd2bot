from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.types.game.house.HouseInformationsInside import HouseInformationsInside


@dataclass
class MapComplementaryInformationsDataInHouseMessage(MapComplementaryInformationsDataMessage):
    currentHouse:HouseInformationsInside
    
    
    def __post_init__(self):
        super().__init__()
    