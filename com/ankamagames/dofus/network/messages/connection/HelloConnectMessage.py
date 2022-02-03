from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HelloConnectMessage(NetworkMessage):
    salt:str
    key:list[int]
    

    def init(self, salt:str, key:list[int]):
        self.salt = salt
        self.key = key
        
        super().__init__()
    
    