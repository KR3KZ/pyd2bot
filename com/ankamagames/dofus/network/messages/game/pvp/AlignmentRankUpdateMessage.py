from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentRankUpdateMessage(NetworkMessage):
    alignmentRank:int
    verbose:bool
    

    def init(self, alignmentRank:int, verbose:bool):
        self.alignmentRank = alignmentRank
        self.verbose = verbose
        
        super().__init__()
    
    