from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage


@dataclass
class MapComplementaryInformationsAnomalyMessage(MapComplementaryInformationsDataMessage):
    level:int
    closingTime:int
    
    
    def __post_init__(self):
        super().__init__()
    