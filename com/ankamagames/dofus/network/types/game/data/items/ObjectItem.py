from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItem(Item):
    position:int
    objectGID:int
    effects:list['ObjectEffect']
    objectUID:int
    quantity:int
    

    def init(self, position:int, objectGID:int, effects:list['ObjectEffect'], objectUID:int, quantity:int):
        self.position = position
        self.objectGID = objectGID
        self.effects = effects
        self.objectUID = objectUID
        self.quantity = quantity
        
        super().__init__()
    
    