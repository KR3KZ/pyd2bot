from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiCancelBidRequestMessage(NetworkMessage):
    id:int
    type:int
    

    def init(self, id:int, type:int):
        self.id = id
        self.type = type
        
        super().__init__()
    
    