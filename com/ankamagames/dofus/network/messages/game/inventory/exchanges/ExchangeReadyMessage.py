from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeReadyMessage(NetworkMessage):
    ready:bool
    step:int
    

    def init(self, ready:bool, step:int):
        self.ready = ready
        self.step = step
        
        super().__init__()
    
    