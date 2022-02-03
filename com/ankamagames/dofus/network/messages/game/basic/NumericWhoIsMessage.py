from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class NumericWhoIsMessage(NetworkMessage):
    playerId:int
    accountId:int
    

    def init(self, playerId:int, accountId:int):
        self.playerId = playerId
        self.accountId = accountId
        
        super().__init__()
    
    