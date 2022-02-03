from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobBookSubscription(NetworkMessage):
    jobId:int
    subscribed:bool
    

    def init(self, jobId:int, subscribed:bool):
        self.jobId = jobId
        self.subscribed = subscribed
        
        super().__init__()
    
    