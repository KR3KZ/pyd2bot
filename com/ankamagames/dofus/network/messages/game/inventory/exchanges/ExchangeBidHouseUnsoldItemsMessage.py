from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity


class ExchangeBidHouseUnsoldItemsMessage(NetworkMessage):
    protocolId = 5576
    items:ObjectItemGenericQuantity
    
