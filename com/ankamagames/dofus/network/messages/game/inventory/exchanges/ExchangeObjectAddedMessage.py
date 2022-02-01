from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ExchangeObjectAddedMessage(ExchangeObjectMessage):
    object:ObjectItem
    
    
