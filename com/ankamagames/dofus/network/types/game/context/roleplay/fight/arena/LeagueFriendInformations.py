from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class LeagueFriendInformations(AbstractContactInformations):
    playerId:int
    playerName:str
    breed:int
    sex:bool
    level:int
    leagueId:int
    totalLeaguePoints:int
    ladderPosition:int
    

    def init(self, playerId:int, playerName:str, breed:int, sex:bool, level:int, leagueId:int, totalLeaguePoints:int, ladderPosition:int, accountId:int, accountTag:'AccountTagInformation'):
        self.playerId = playerId
        self.playerName = playerName
        self.breed = breed
        self.sex = sex
        self.level = level
        self.leagueId = leagueId
        self.totalLeaguePoints = totalLeaguePoints
        self.ladderPosition = ladderPosition
        
        super().__init__(accountId, accountTag)
    
    