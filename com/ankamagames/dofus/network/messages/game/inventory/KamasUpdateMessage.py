from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class KamasUpdateMessage(NetworkMessage):
    kamasTotal:int
    

    def init(self, kamasTotal:int):
        self.kamasTotal = kamasTotal
        
        super().__init__()
    
    