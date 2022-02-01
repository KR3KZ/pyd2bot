from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ArenaRanking(INetworkMessage):
    protocolId = 6311
    rank:int
    bestRank:int
    
    
