from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryListRequestMessage(NetworkMessage):
    jobId:int
    

    def init(self, jobId:int):
        self.jobId = jobId
        
        super().__init__()
    
    