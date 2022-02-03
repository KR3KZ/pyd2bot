from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockSellRequestMessage(NetworkMessage):
    price:int
    forSale:bool
    

    def init(self, price:int, forSale:bool):
        self.price = price
        self.forSale = forSale
        
        super().__init__()
    
    