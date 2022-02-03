from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PaddockSellBuyDialogMessage(NetworkMessage):
    bsell:bool
    ownerId:int
    price:int
    

    def init(self, bsell:bool, ownerId:int, price:int):
        self.bsell = bsell
        self.ownerId = ownerId
        self.price = price
        
        super().__init__()
    
    