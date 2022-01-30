from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeCraftResultMessage import ExchangeCraftResultMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemNotInContainer import ObjectItemNotInContainer


class ExchangeCraftResultWithObjectDescMessage(ExchangeCraftResultMessage):
    protocolId = 118
    objectInfo:ObjectItemNotInContainer
    
    
