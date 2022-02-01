from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectsRemovedMessage(ExchangeObjectMessage):
    objectUID:list[int]
    
    
