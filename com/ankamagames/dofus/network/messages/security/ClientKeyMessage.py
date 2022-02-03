from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ClientKeyMessage(NetworkMessage):
    key:str
    

    def init(self, key:str):
        self.key = key
        
        super().__init__()
    
    