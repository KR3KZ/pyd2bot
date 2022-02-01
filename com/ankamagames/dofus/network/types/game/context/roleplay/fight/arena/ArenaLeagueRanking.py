from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ArenaLeagueRanking(INetworkMessage):
    protocolId = 2820
    rank:int
    leagueId:int
    leaguePoints:int
    totalLeaguePoints:int
    ladderPosition:int
    
    
