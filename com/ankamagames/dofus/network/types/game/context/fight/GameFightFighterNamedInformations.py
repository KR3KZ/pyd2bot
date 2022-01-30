from com.ankamagames.dofus.network.types.game.context.fight.GameFightFighterInformations import GameFightFighterInformations
from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus


class GameFightFighterNamedInformations(GameFightFighterInformations):
    protocolId = 7293
    name:str
    status:PlayerStatus
    leagueId:int
    ladderPosition:int
    hiddenInPrefight:bool
    
