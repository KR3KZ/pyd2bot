from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


class ExchangeShopStockStartedMessage(NetworkMessage):
    protocolId = 2502
    objectsInfos:list[ObjectItemToSell]
    
