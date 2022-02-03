from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateSelfAgressableStatusMessage(NetworkMessage):
    status:int
    probationTime:int
    

    def init(self, status:int, probationTime:int):
        self.status = status
        self.probationTime = probationTime
        
        super().__init__()
    
    