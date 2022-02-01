from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedMessage import ExchangeRequestedMessage


class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
    source:int
    target:int
    
    
