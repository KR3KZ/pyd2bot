from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HaapiSessionMessage(NetworkMessage):
    key:str
    type:int
    

    def init(self, key:str, type:int):
        self.key = key
        self.type = type
        
        super().__init__()
    
    