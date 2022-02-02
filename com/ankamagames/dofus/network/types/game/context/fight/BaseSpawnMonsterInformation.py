from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


@dataclass
class BaseSpawnMonsterInformation(SpawnInformation):
    creatureGenericId:int
    
    
    def __post_init__(self):
        super().__init__()
    