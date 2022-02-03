from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeKamaModifiedMessage(ExchangeObjectMessage):
    quantity:int
    

    def init(self, quantity:int, remote:bool):
        self.quantity = quantity
        
        super().__init__(remote)
    
    