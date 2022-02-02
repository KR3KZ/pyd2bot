from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations


@dataclass
class LeagueFriendInformations(AbstractContactInformations):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    leagueId:int
    totalLeaguePoints:int
    ladderPosition:int
    
    
    def __post_init__(self):
        super().__init__()
    