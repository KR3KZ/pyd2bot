from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics


@dataclass
class GameFightFighterInformations(GameContextActorInformations):
    spawnInfo:GameContextBasicSpawnInformation
    wave:int
    stats:GameFightCharacteristics
    previousPositions:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    