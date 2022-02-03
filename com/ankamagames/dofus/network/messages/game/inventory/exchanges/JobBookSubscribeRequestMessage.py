from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobBookSubscribeRequestMessage(NetworkMessage):
    jobIds:list[int]
    

    def init(self, jobIds:list[int]):
        self.jobIds = jobIds
        
        super().__init__()
    
    