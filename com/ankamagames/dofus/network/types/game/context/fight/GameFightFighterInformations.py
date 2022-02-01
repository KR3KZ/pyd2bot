from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics


class GameFightFighterInformations(GameContextActorInformations):
    spawnInfo:GameContextBasicSpawnInformation
    wave:int
    stats:GameFightCharacteristics
    previousPositions:list[int]
    
    
