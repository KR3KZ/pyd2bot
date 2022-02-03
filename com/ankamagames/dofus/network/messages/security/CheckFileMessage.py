from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckFileMessage(NetworkMessage):
    filenameHash:str
    type:int
    value:str
    

    def init(self, filenameHash:str, type:int, value:str):
        self.filenameHash = filenameHash
        self.type = type
        self.value = value
        
        super().__init__()
    
    