from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


class ExchangeShopStockMovementUpdatedMessage(INetworkMessage):
    protocolId = 9932
    objectInfo:ObjectItemToSell
    
    
