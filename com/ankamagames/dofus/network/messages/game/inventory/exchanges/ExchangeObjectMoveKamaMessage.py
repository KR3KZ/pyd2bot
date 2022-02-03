from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class ExchangeObjectMoveKamaMessage(NetworkMessage):
    quantity:int
    

    def init(self, quantity:int):
        self.quantity = quantity
        
        super().__init__()
    
    