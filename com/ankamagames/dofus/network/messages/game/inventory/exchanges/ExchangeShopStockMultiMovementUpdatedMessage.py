from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


class ExchangeShopStockMultiMovementUpdatedMessage(INetworkMessage):
    protocolId = 8646
    objectInfoList:ObjectItemToSell
    
    
