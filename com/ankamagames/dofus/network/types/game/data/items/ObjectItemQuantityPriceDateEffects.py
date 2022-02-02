from dataclasses import dataclass
from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from com.ankamagames.dofus.network.types.game.data.items.ObjectEffects import ObjectEffects


@dataclass
class ObjectItemQuantityPriceDateEffects(ObjectItemGenericQuantity):
    price:int
    effects:ObjectEffects
    date:int
    
    
    def __post_init__(self):
        super().__init__()
    