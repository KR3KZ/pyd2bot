from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectRemovedMessage(ExchangeObjectMessage):
    protocolId = 7006
    objectUID:int
    
    
