from com.ankamagames.dofus.network.types.game.friend.AbstractContactInformations import AbstractContactInformations


class FriendInformations(AbstractContactInformations):
    protocolId = 8035
    playerState:int
    lastConnection:int
    achievementPoints:int
    leagueId:int
    ladderPosition:int
    
    
