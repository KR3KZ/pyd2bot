from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolSelectRequestMessage(NetworkMessage):
    idolId:int
    activate:bool
    party:bool
    

    def init(self, idolId:int):
        self.idolId = idolId
        
        super().__init__()
    
    