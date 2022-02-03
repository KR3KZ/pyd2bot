from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemToSellInHumanVendorShop(Item):
    objectGID:int
    effects:list['ObjectEffect']
    objectUID:int
    quantity:int
    objectPrice:int
    publicPrice:int
    

    def init(self, objectGID:int, effects:list['ObjectEffect'], objectUID:int, quantity:int, objectPrice:int, publicPrice:int):
        self.objectGID = objectGID
        self.effects = effects
        self.objectUID = objectUID
        self.quantity = quantity
        self.objectPrice = objectPrice
        self.publicPrice = publicPrice
        
        super().__init__()
    
    