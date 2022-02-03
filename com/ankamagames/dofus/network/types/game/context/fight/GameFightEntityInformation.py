from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightEntityInformation(GameFightFighterInformations):
    entityModelId:int
    level:int
    masterId:int
    

    def init(self, entityModelId:int, level:int, masterId:int, spawnInfo:'GameContextBasicSpawnInformation', wave:int, stats:'GameFightCharacteristics', previousPositions:list[int], look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.entityModelId = entityModelId
        self.level = level
        self.masterId = masterId
        
        super().__init__(spawnInfo, wave, stats, previousPositions, look, contextualId, disposition)
    
    