from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeIsReadyMessage(NetworkMessage):
    id:int
    ready:bool
    

    def init(self, id:int, ready:bool):
        self.id = id
        self.ready = ready
        
        super().__init__()
    
    