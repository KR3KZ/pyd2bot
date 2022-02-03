from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaLeagueRewardsMessage(NetworkMessage):
    seasonId:int
    leagueId:int
    ladderPosition:int
    endSeasonReward:bool
    

    def init(self, seasonId:int, leagueId:int, ladderPosition:int, endSeasonReward:bool):
        self.seasonId = seasonId
        self.leagueId = leagueId
        self.ladderPosition = ladderPosition
        self.endSeasonReward = endSeasonReward
        
        super().__init__()
    
    