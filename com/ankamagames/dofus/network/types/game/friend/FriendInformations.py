from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations


@dataclass
class FriendInformations(AbstractContactInformations):
    playerState:int
    lastConnection:int
    achievementPoints:int
    leagueId:int
    ladderPosition:int
    
    
    def __post_init__(self):
        super().__init__()
    