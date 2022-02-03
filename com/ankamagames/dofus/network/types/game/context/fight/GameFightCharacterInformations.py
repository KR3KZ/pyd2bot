from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.alignment.ActorAlignmentInformations import ActorAlignmentInformations
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightCharacterInformations(GameFightFighterNamedInformations):
    level:int
    alignmentInfos:'ActorAlignmentInformations'
    breed:int
    sex:bool
    

    def init(self, level:int, alignmentInfos:'ActorAlignmentInformations', breed:int, sex:bool, name:str, status:'PlayerStatus', leagueId:int, ladderPosition:int, hiddenInPrefight:bool, spawnInfo:'GameContextBasicSpawnInformation', wave:int, stats:'GameFightCharacteristics', previousPositions:list[int], look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.level = level
        self.alignmentInfos = alignmentInfos
        self.breed = breed
        self.sex = sex
        
        super().__init__(name, status, leagueId, ladderPosition, hiddenInPrefight, spawnInfo, wave, stats, previousPositions, look, contextualId, disposition)
    
    