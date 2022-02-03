from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableUseCodeMessage(NetworkMessage):
    code:str
    

    def init(self, code:str):
        self.code = code
        
        super().__init__()
    
    