from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class HouseBuyRequestMessage(NetworkMessage):
    proposedPrice:int
    

    def init(self, proposedPrice:int):
        self.proposedPrice = proposedPrice
        
        super().__init__()
    
    