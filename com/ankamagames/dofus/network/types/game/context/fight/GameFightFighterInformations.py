from com.ankamagames.dofus.network.types.game.context.GameContextActorInformations import GameContextActorInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightFighterInformations(GameContextActorInformations):
    spawnInfo:'GameContextBasicSpawnInformation'
    wave:int
    stats:'GameFightCharacteristics'
    previousPositions:list[int]
    

    def init(self, spawnInfo:'GameContextBasicSpawnInformation', wave:int, stats:'GameFightCharacteristics', previousPositions:list[int], look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.spawnInfo = spawnInfo
        self.wave = wave
        self.stats = stats
        self.previousPositions = previousPositions
        
        super().__init__(look, contextualId, disposition)
    
    