from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ArenaRanking(NetworkMessage):
    rank:int
    bestRank:int
    

    def init(self, rank:int, bestRank:int):
        self.rank = rank
        self.bestRank = bestRank
        
        super().__init__()
    
    