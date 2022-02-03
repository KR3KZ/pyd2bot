from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountSetXpRatioRequestMessage(NetworkMessage):
    xpRatio:int
    

    def init(self, xpRatio:int):
        self.xpRatio = xpRatio
        
        super().__init__()
    
    