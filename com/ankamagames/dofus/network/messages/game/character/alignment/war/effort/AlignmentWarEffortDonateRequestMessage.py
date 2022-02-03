from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonateRequestMessage(NetworkMessage):
    donation:int
    

    def init(self, donation:int):
        self.donation = donation
        
        super().__init__()
    
    