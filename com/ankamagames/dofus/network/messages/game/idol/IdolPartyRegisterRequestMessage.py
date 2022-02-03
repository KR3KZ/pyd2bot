from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IdolPartyRegisterRequestMessage(NetworkMessage):
    register:bool
    

    def init(self, register:bool):
        self.register = register
        
        super().__init__()
    
    