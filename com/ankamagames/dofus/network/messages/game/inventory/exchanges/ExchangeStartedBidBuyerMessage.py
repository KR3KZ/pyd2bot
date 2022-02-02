from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.SellerBuyerDescriptor import SellerBuyerDescriptor


@dataclass
class ExchangeStartedBidBuyerMessage(NetworkMessage):
    buyerDescriptor:SellerBuyerDescriptor
    
    
    def __post_init__(self):
        super().__init__()
    