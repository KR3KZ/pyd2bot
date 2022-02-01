from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(INetworkMessage):
    protocolId = 2090
    seasonId:int
    leagueId:int
    ladderPosition:int
    endSeasonReward:bool
    
    
