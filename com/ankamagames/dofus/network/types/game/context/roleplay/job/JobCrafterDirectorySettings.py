from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectorySettings(NetworkMessage):
    jobId:int
    minLevel:int
    free:bool
    

    def init(self, jobId:int, minLevel:int, free:bool):
        self.jobId = jobId
        self.minLevel = minLevel
        self.free = free
        
        super().__init__()
    
    