from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ArenaLeagueRanking(INetworkMessage):
    protocolId = 2820
    rank:int
    leagueId:int
    leaguePoints:int
    totalLeaguePoints:int
    ladderPosition:int
    
    
