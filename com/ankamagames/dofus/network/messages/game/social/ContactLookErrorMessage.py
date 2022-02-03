from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ContactLookErrorMessage(NetworkMessage):
    requestId:int
    

    def init(self, requestId:int):
        self.requestId = requestId
        
        super().__init__()
    
    