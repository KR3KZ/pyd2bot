from dataclasses import dataclass
from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop


@dataclass
class ExchangeStartOkHumanVendorMessage(NetworkMessage):
    sellerId:int
    objectsInfos:list[ObjectItemToSellInHumanVendorShop]
    
    
    def __post_init__(self):
        super().__init__()
    