from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.SpawnInformation import SpawnInformation


@dataclass
class SpawnCompanionInformation(SpawnInformation):
    modelId:int
    level:int
    summonerId:int
    ownerId:int
    
    
    def __post_init__(self):
        super().__init__()
    