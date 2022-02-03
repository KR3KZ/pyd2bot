from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ConsoleMessage(NetworkMessage):
    type:int
    content:str
    

    def init(self, type:int, content:str):
        self.type = type
        self.content = content
        
        super().__init__()
    
    