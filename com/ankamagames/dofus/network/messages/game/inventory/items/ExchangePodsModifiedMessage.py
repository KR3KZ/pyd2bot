from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangePodsModifiedMessage(ExchangeObjectMessage):
    currentWeight:int
    maxWeight:int
    
    
