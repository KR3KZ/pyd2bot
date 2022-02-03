from com.ankamagames.dofus.network.types.game.friend.FriendInformations import FriendInformations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.context.roleplay.GuildInformations import GuildInformations
    from com.ankamagames.dofus.network.types.game.character.status.PlayerStatus import PlayerStatus
    from com.ankamagames.dofus.network.types.common.AccountTagInformation import AccountTagInformation
    


class FriendOnlineInformations(FriendInformations):
    playerId:int
    playerName:str
    level:int
    alignmentSide:int
    breed:int
    guildInfo:'GuildInformations'
    moodSmileyId:int
    status:'PlayerStatus'
    sex:bool
    havenBagShared:bool
    

    def init(self, playerId:int, playerName:str, level:int, alignmentSide:int, breed:int, guildInfo:'GuildInformations', moodSmileyId:int, status:'PlayerStatus', playerState:int, lastConnection:int, achievementPoints:int, leagueId:int, ladderPosition:int, accountId:int, accountTag:'AccountTagInformation'):
        self.playerId = playerId
        self.playerName = playerName
        self.level = level
        self.alignmentSide = alignmentSide
        self.breed = breed
        self.guildInfo = guildInfo
        self.moodSmileyId = moodSmileyId
        self.status = status
        
        super().__init__(playerState, lastConnection, achievementPoints, leagueId, ladderPosition, accountId, accountTag)
    
    