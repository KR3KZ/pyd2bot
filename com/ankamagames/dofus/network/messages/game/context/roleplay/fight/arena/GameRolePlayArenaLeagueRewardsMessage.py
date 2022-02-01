from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(NetworkMessage):
    seasonId:int
    leagueId:int
    ladderPosition:int
    endSeasonReward:bool
    
    
