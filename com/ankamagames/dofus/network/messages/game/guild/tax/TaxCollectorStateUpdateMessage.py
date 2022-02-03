from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TaxCollectorStateUpdateMessage(NetworkMessage):
    uniqueId:int
    state:int
    

    def init(self, uniqueId:int, state:int):
        self.uniqueId = uniqueId
        self.state = state
        
        super().__init__()
    
    