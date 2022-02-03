from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeWaitingResultMessage(NetworkMessage):
    bwait:bool
    

    def init(self, bwait:bool):
        self.bwait = bwait
        
        super().__init__()
    
    