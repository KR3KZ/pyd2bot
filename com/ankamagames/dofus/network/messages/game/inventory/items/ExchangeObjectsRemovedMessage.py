from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectsRemovedMessage(ExchangeObjectMessage):
    protocolId = 4841
    objectUID:int
    
    
