from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeReadyMessage import ExchangeReadyMessage


class FocusedExchangeReadyMessage(ExchangeReadyMessage):
    focusActionId:int
    

    def init(self, focusActionId:int, ready:bool, step:int):
        self.focusActionId = focusActionId
        
        super().__init__(ready, step)
    
    