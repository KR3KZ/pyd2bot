from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem


class ExchangeObjectModifiedMessage(ExchangeObjectMessage):
    protocolId = 3598
    object:ObjectItem
    
    
