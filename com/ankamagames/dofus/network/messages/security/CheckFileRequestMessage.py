from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CheckFileRequestMessage(NetworkMessage):
    filename:str
    type:int
    

    def init(self, filename:str, type:int):
        self.filename = filename
        self.type = type
        
        super().__init__()
    
    