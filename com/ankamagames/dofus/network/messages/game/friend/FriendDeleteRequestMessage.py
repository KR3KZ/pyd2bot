from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class FriendDeleteRequestMessage(NetworkMessage):
    accountId:int
    

    def init(self, accountId:int):
        self.accountId = accountId
        
        super().__init__()
    
    