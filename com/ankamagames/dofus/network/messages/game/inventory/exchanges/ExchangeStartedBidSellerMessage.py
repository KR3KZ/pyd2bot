from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid


class ExchangeStartedBidSellerMessage(NetworkMessage):
    sellerDescriptor:SellerBuyerDescriptor
    objectsInfos:list[ObjectItemToSellInBid]
    
    
