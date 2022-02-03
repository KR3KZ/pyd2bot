from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AuthenticationTicketMessage(NetworkMessage):
    lang:str
    ticket:str
    

    def init(self, lang:str, ticket:str):
        self.lang = lang
        self.ticket = ticket
        
        super().__init__()
    
    