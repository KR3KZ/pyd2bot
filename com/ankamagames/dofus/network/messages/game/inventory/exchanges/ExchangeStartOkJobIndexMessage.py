from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeStartOkJobIndexMessage(NetworkMessage):
    jobs:list[int]
    

    def init(self, jobs:list[int]):
        self.jobs = jobs
        
        super().__init__()
    
    