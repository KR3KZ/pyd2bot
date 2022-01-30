from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ArenaLeagueRanking(NetworkMessage):
    protocolId = 2820
    rank:int
    leagueId:int
    leaguePoints:int
    totalLeaguePoints:int
    ladderPosition:int
    
    
