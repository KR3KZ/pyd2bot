from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid


class ExchangeStartedBidSellerMessage(NetworkMessage):
    protocolId = 7532
    sellerDescriptor:SellerBuyerDescriptor
    objectsInfos:ObjectItemToSellInBid
    
    
