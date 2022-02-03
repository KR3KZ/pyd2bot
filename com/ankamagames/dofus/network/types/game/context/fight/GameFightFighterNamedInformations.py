from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.game.context.fight.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
    from com.ankamagames.dofus.network.types.game.context.fight.GameFightCharacteristics import GameFightCharacteristics
    from com.ankamagames.dofus.network.types.game.look.EntityLook import EntityLook
    from com.ankamagames.dofus.network.types.game.context.EntityDispositionInformations import EntityDispositionInformations
    


class GameFightFighterNamedInformations(GameFightFighterInformations):
    name:str
    status:'PlayerStatus'
    leagueId:int
    ladderPosition:int
    hiddenInPrefight:bool
    

    def init(self, name:str, status:'PlayerStatus', leagueId:int, ladderPosition:int, hiddenInPrefight:bool, spawnInfo:'GameContextBasicSpawnInformation', wave:int, stats:'GameFightCharacteristics', previousPositions:list[int], look:'EntityLook', contextualId:int, disposition:'EntityDispositionInformations'):
        self.name = name
        self.status = status
        self.leagueId = leagueId
        self.ladderPosition = ladderPosition
        self.hiddenInPrefight = hiddenInPrefight
        
        super().__init__(spawnInfo, wave, stats, previousPositions, look, contextualId, disposition)
    
    