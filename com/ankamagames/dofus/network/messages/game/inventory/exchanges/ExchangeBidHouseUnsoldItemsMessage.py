from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity


class ExchangeBidHouseUnsoldItemsMessage(INetworkMessage):
    protocolId = 5576
    items:ObjectItemGenericQuantity
    
    
