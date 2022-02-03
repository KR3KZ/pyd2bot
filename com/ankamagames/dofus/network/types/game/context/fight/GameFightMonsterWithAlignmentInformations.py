from com.ankamagames.dofus.network.types.game.context.fight.GameFightMonsterInformations import GameFightMonsterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
    alignmentInfos:'ActorAlignmentInformations'
    

    def init(self, alignmentInfos:'ActorAlignmentInformations', creatureGenericId:int, creatureGrade:int, creatureLevel:int, spawnInfo:'GameContextBasicSpawnInformation', wave:int, stats:'GameFightCharacteristics', previousPositions:list[int], look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.alignmentInfos = alignmentInfos
        
        super().__init__(creatureGenericId, creatureGrade, creatureLevel, spawnInfo, wave, stats, previousPositions, look, contextualId, disposition)
    
    