from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid


class ExchangeStartedBidSellerMessage(INetworkMessage):
    protocolId = 7532
    sellerDescriptor:SellerBuyerDescriptor
    objectsInfos:ObjectItemToSellInBid
    
    
