from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountXpRatioMessage(NetworkMessage):
    ratio:int
    

    def init(self, ratio:int):
        self.ratio = ratio
        
        super().__init__()
    
    