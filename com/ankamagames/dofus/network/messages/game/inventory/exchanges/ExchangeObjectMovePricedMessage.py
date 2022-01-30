from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMoveMessage import ExchangeObjectMoveMessage


class ExchangeObjectMovePricedMessage(ExchangeObjectMoveMessage):
    protocolId = 1384
    price:int
    
