from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MountInformationRequestMessage(NetworkMessage):
    id:int
    time:int
    

    def init(self, id:int, time:int):
        self.id = id
        self.time = time
        
        super().__init__()
    
    