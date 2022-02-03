from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectMessage(NetworkMessage):
    remote:bool
    

    def init(self, remote:bool):
        self.remote = remote
        
        super().__init__()
    
    