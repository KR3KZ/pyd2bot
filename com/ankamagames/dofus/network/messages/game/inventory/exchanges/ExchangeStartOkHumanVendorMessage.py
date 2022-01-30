from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop


class ExchangeStartOkHumanVendorMessage(NetworkMessage):
    protocolId = 9011
    sellerId:float
    objectsInfos:list[ObjectItemToSellInHumanVendorShop]
    
