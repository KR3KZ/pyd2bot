from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyMessage(NetworkMessage):
    uid:int
    qty:int
    price:int
    

    def init(self, uid:int, qty:int, price:int):
        self.uid = uid
        self.qty = qty
        self.price = price
        
        super().__init__()
    
    