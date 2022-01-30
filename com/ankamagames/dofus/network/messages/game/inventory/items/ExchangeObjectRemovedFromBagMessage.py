from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectRemovedFromBagMessage(ExchangeObjectMessage):
    protocolId = 1851
    objectUID:int
    
