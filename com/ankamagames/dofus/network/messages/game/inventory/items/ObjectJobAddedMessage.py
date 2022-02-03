from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ObjectJobAddedMessage(NetworkMessage):
    jobId:int
    

    def init(self, jobId:int):
        self.jobId = jobId
        
        super().__init__()
    
    