from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class StorageKamasUpdateMessage(NetworkMessage):
    kamasTotal:int
    

    def init(self, kamasTotal:int):
        self.kamasTotal = kamasTotal
        
        super().__init__()
    
    