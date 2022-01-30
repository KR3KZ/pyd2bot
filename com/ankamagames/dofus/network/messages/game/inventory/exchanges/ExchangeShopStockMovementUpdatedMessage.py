from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


class ExchangeShopStockMovementUpdatedMessage(NetworkMessage):
    protocolId = 9932
    objectInfo:ObjectItemToSell
    
    
