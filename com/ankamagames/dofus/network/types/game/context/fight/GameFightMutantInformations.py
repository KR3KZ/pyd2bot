from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightMutantInformations(GameFightFighterNamedInformations):
    powerLevel:int
    

    def init(self, powerLevel:int, name:str, status:'PlayerStatus', leagueId:int, ladderPosition:int, hiddenInPrefight:bool, spawnInfo:'GameContextBasicSpawnInformation', wave:int, stats:'GameFightCharacteristics', previousPositions:list[int], look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.powerLevel = powerLevel
        
        super().__init__(name, status, leagueId, ladderPosition, hiddenInPrefight, spawnInfo, wave, stats, previousPositions, look, contextualId, disposition)
    
    