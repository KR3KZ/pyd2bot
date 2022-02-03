from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AdminCommandMessage(NetworkMessage):
    content:str
    

    def init(self, content:str):
        self.content = content
        
        super().__init__()
    
    