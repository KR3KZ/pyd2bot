from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class IgnoredDeleteRequestMessage(NetworkMessage):
    accountId:int
    session:bool
    

    def init(self, accountId:int, session:bool):
        self.accountId = accountId
        self.session = session
        
        super().__init__()
    
    