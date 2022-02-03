from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolSelectErrorMessage(NetworkMessage):
    reason:int
    idolId:int
    activate:bool
    party:bool
    

    def init(self, reason:int, idolId:int):
        self.reason = reason
        self.idolId = idolId
        
        super().__init__()
    
    