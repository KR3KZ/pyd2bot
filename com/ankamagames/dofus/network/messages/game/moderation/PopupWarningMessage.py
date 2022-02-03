from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PopupWarningMessage(NetworkMessage):
    lockDuration:int
    author:str
    content:str
    

    def init(self, lockDuration:int, author:str, content:str):
        self.lockDuration = lockDuration
        self.author = author
        self.content = content
        
        super().__init__()
    
    