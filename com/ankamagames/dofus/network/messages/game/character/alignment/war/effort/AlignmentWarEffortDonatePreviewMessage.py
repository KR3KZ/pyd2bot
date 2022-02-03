from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AlignmentWarEffortDonatePreviewMessage(NetworkMessage):
    xp:int
    

    def init(self, xp:int):
        self.xp = xp
        
        super().__init__()
    
    