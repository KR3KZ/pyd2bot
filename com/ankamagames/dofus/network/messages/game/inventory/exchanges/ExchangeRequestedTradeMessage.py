from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedMessage import ExchangeRequestedMessage


class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
    source:int
    target:int
    

    def init(self, source:int, target:int, exchangeType:int):
        self.source = source
        self.target = target
        
        super().__init__(exchangeType)
    
    