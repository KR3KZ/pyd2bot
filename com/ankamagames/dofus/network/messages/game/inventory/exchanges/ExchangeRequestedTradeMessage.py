from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestedMessage import ExchangeRequestedMessage


class ExchangeRequestedTradeMessage(ExchangeRequestedMessage):
    protocolId = 9612
    source:float
    target:float
    
