from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerRequestMessage(ExchangeRequestMessage):
    target:int
    

    def init(self, target:int, exchangeType:int):
        self.target = target
        
        super().__init__(exchangeType)
    
    