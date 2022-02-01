from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


class ExchangeShopStockStartedMessage(INetworkMessage):
    protocolId = 2502
    objectsInfos:ObjectItemToSell
    
    
