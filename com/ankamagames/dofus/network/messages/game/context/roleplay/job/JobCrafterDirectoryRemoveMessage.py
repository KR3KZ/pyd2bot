from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryRemoveMessage(NetworkMessage):
    jobId:int
    playerId:int
    

    def init(self, jobId:int, playerId:int):
        self.jobId = jobId
        self.playerId = playerId
        
        super().__init__()
    
    