from dataclasses import dataclass
from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeBidPriceMessage import ExchangeBidPriceMessage


@dataclass
class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
    allIdentical:bool
    minimalPrices:list[int]
    
    
    def __post_init__(self):
        super().__init__()
    