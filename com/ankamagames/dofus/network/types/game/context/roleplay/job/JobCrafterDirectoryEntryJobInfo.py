from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryJobInfo(NetworkMessage):
    jobId:int
    jobLevel:int
    free:bool
    minLevel:int
    

    def init(self, jobId:int, jobLevel:int, free:bool, minLevel:int):
        self.jobId = jobId
        self.jobLevel = jobLevel
        self.free = free
        self.minLevel = minLevel
        
        super().__init__()
    
    