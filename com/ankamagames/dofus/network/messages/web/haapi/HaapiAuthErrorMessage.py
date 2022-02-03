from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiAuthErrorMessage(NetworkMessage):
    type:int
    

    def init(self, type:int):
        self.type = type
        
        super().__init__()
    
    