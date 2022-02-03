from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class WrapperObjectDissociateRequestMessage(NetworkMessage):
    hostUID:int
    hostPos:int
    

    def init(self, hostUID:int, hostPos:int):
        self.hostUID = hostUID
        self.hostPos = hostPos
        
        super().__init__()
    
    