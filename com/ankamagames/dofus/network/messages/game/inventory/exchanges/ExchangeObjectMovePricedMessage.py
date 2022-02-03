from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMoveMessage import ExchangeObjectMoveMessage


class ExchangeObjectMovePricedMessage(ExchangeObjectMoveMessage):
    price:int
    

    def init(self, price:int, objectUID:int, quantity:int):
        self.price = price
        
        super().__init__(objectUID, quantity)
    
    