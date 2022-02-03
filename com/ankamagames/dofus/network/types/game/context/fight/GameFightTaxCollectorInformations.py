from com.ankamagames.dofus.network.types.game.context.fight.GameFightAIInformations import GameFightAIInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightTaxCollectorInformations(GameFightAIInformations):
    firstNameId:int
    lastNameId:int
    level:int
    

    def init(self, firstNameId:int, lastNameId:int, level:int, spawnInfo:'GameContextBasicSpawnInformation', wave:int, stats:'GameFightCharacteristics', previousPositions:list[int], look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.firstNameId = firstNameId
        self.lastNameId = lastNameId
        self.level = level
        
        super().__init__(spawnInfo, wave, stats, previousPositions, look, contextualId, disposition)
    
    