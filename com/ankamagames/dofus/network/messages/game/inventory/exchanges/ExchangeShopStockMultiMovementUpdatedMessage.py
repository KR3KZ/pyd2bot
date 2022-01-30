from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


class ExchangeShopStockMultiMovementUpdatedMessage(NetworkMessage):
    protocolId = 8646
    objectInfoList:ObjectItemToSell
    
    
