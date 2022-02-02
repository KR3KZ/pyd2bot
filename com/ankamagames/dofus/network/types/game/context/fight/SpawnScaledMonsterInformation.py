from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation


@dataclass
class SpawnScaledMonsterInformation(BaseSpawnMonsterInformation):
    creatureLevel:int
    
    
    def __post_init__(self):
        super().__init__()
    