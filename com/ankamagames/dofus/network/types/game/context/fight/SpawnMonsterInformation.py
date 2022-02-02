from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation


@dataclass
class SpawnMonsterInformation(BaseSpawnMonsterInformation):
    creatureGrade:int
    
    
    def __post_init__(self):
        super().__init__()
    