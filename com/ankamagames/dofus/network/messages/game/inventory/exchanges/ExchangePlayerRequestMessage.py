from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerRequestMessage(ExchangeRequestMessage):
    protocolId = 2400
    target:int
    
    
