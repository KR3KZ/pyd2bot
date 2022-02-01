from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor


class ExchangeStartedBidBuyerMessage(NetworkMessage):
    buyerDescriptor:SellerBuyerDescriptor
    
    
