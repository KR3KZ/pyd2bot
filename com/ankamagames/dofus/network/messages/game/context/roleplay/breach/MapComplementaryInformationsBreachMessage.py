from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.context.roleplay.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage
from com.ankamagames.dofus.network.types.game.context.roleplay.breach.BreachBranch import BreachBranch


@dataclass
class MapComplementaryInformationsBreachMessage(MapComplementaryInformationsDataMessage):
    floor:int
    room:int
    infinityMode:int
    branches:list[BreachBranch]
    
    
    def __post_init__(self):
        super().__init__()
    