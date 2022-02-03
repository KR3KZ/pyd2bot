from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockBuyableInformations(NetworkMessage):
    price:int
    locked:bool
    

    def init(self, price:int, locked:bool):
        self.price = price
        self.locked = locked
        
        super().__init__()
    
    