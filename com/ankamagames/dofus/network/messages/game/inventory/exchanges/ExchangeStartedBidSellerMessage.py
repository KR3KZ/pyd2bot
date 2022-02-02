from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInBid import ObjectItemToSellInBid


@dataclass
class ExchangeStartedBidSellerMessage(NetworkMessage):
    sellerDescriptor:SellerBuyerDescriptor
    objectsInfos:list[ObjectItemToSellInBid]
    
    
    def __post_init__(self):
        super().__init__()
    