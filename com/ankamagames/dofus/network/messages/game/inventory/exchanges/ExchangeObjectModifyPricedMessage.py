from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMovePricedMessage import ExchangeObjectMovePricedMessage


class ExchangeObjectModifyPricedMessage(ExchangeObjectMovePricedMessage):
    

    def init(self, price:int, objectUID:int, quantity:int):
        
        super().__init__(price, objectUID, quantity)
    
    