from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolPartyLostMessage(NetworkMessage):
    idolId:int
    

    def init(self, idolId:int):
        self.idolId = idolId
        
        super().__init__()
    
    