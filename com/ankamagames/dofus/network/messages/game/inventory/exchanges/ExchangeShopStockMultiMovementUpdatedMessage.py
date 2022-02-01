from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


class ExchangeShopStockMultiMovementUpdatedMessage(NetworkMessage):
    objectInfoList:list[ObjectItemToSell]
    
    
