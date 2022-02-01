from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ArenaLeagueRanking(NetworkMessage):
    rank:int
    leagueId:int
    leaguePoints:int
    totalLeaguePoints:int
    ladderPosition:int
    
    
