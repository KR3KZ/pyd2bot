from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(INetworkMessage):
    protocolId = 2090
    seasonId:int
    leagueId:int
    ladderPosition:int
    endSeasonReward:bool
    
    
