from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class RecycledItem(NetworkMessage):
    id:int
    qty:int
    

    def init(self, id:int, qty:int):
        self.id = id
        self.qty = qty
        
        super().__init__()
    
    