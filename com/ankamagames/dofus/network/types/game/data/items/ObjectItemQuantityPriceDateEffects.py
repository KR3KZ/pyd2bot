from com.ankamagames.dofus.network.types.game.data.items.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectEffects import ObjectEffects
    


class ObjectItemQuantityPriceDateEffects(ObjectItemGenericQuantity):
    price:int
    effects:'ObjectEffects'
    date:int
    

    def init(self, price:int, effects:'ObjectEffects', date:int, objectGID:int, quantity:int):
        self.price = price
        self.effects = effects
        self.date = date
        
        super().__init__(objectGID, quantity)
    
    