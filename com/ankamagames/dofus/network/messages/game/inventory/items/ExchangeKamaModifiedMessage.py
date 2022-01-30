from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeKamaModifiedMessage(ExchangeObjectMessage):
    protocolId = 1705
    quantity:float
    
