from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class DebtInformation(NetworkMessage):
    id:int
    timestamp:int
    

    def init(self, id:int, timestamp:int):
        self.id = id
        self.timestamp = timestamp
        
        super().__init__()
    
    