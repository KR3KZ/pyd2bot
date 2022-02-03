from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ReloginTokenStatusMessage(NetworkMessage):
    validToken:bool
    ticket:list[int]
    

    def init(self, validToken:bool, ticket:list[int]):
        self.validToken = validToken
        self.ticket = ticket
        
        super().__init__()
    
    