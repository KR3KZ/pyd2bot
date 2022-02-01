from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop


class ExchangeStartOkHumanVendorMessage(INetworkMessage):
    protocolId = 9011
    sellerId:int
    objectsInfos:ObjectItemToSellInHumanVendorShop
    
    
