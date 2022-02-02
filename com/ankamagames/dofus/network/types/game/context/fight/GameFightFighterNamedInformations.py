from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


@dataclass
class GameFightFighterNamedInformations(GameFightFighterInformations):
    name:str
    status:PlayerStatus
    leagueId:int
    ladderPosition:int
    hiddenInPrefight:bool
    
    
    def __post_init__(self):
        super().__init__()
    