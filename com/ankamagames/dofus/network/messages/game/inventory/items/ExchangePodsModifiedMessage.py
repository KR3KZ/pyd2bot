from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangePodsModifiedMessage(ExchangeObjectMessage):
    protocolId = 7130
    currentWeight:int
    maxWeight:int
    
    
