from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CurrentServerStatusUpdateMessage(NetworkMessage):
    status:int
    

    def init(self, status:int):
        self.status = status
        
        super().__init__()
    
    