from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ExchangeObjectsAddedMessage(ExchangeObjectMessage):
    protocolId = 6503
    object:ObjectItem
    
    
