from com.ankamagames.dofus.network.types.game.data.items.ObjectItemMinimalInformation import ObjectItemMinimalInformation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemInformationWithQuantity(ObjectItemMinimalInformation):
    quantity:int
    

    def init(self, quantity:int, objectGID:int, effects:list['ObjectEffect']):
        self.quantity = quantity
        
        super().__init__(objectGID, effects)
    
    