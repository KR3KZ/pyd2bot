from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ArenaLeagueRanking(NetworkMessage):
    rank:int
    leagueId:int
    leaguePoints:int
    totalLeaguePoints:int
    ladderPosition:int
    

    def init(self, rank:int, leagueId:int, leaguePoints:int, totalLeaguePoints:int, ladderPosition:int):
        self.rank = rank
        self.leagueId = leagueId
        self.leaguePoints = leaguePoints
        self.totalLeaguePoints = totalLeaguePoints
        self.ladderPosition = ladderPosition
        
        super().__init__()
    
    