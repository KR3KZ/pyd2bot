from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockInformations(NetworkMessage):
    maxOutdoorMount:int
    maxItems:int
    

    def init(self, maxOutdoorMount:int, maxItems:int):
        self.maxOutdoorMount = maxOutdoorMount
        self.maxItems = maxItems
        
        super().__init__()
    
    