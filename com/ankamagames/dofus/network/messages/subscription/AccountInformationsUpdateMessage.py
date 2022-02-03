from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class AccountInformationsUpdateMessage(NetworkMessage):
    subscriptionEndDate:int
    

    def init(self, subscriptionEndDate:int):
        self.subscriptionEndDate = subscriptionEndDate
        
        super().__init__()
    
    