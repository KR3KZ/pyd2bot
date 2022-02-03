from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class FriendInformations(AbstractContactInformations):
    playerState:int
    lastConnection:int
    achievementPoints:int
    leagueId:int
    ladderPosition:int
    

    def init(self, playerState:int, lastConnection:int, achievementPoints:int, leagueId:int, ladderPosition:int, accountId:int, accountTag:'AccountTagInformation'):
        self.playerState = playerState
        self.lastConnection = lastConnection
        self.achievementPoints = achievementPoints
        self.leagueId = leagueId
        self.ladderPosition = ladderPosition
        
        super().__init__(accountId, accountTag)
    
    