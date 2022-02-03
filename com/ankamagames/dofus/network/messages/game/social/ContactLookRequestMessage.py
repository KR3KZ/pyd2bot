from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ContactLookRequestMessage(NetworkMessage):
    requestId:int
    contactType:int
    

    def init(self, requestId:int, contactType:int):
        self.requestId = requestId
        self.contactType = contactType
        
        super().__init__()
    
    