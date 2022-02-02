from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemToSell import ObjectItemToSell


@dataclass
class ObjectItemToSellInBid(ObjectItemToSell):
    unsoldDelay:int
    
    
    def __post_init__(self):
        super().__init__()
    