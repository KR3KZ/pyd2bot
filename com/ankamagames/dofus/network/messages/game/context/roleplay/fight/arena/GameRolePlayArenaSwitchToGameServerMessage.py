from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaSwitchToGameServerMessage(NetworkMessage):
    validToken:bool
    ticket:list[int]
    homeServerId:int
    

    def init(self, validToken:bool, ticket:list[int], homeServerId:int):
        self.validToken = validToken
        self.ticket = ticket
        self.homeServerId = homeServerId
        
        super().__init__()
    
    