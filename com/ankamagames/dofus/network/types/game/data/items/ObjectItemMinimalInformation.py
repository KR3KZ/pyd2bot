from com.ankamagames.dofus.network.types.game.data.items.Item import Item
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.effects.ObjectEffect import ObjectEffect
    


class ObjectItemMinimalInformation(Item):
    objectGID:int
    effects:list['ObjectEffect']
    

    def init(self, objectGID:int, effects:list['ObjectEffect']):
        self.objectGID = objectGID
        self.effects = effects
        
        super().__init__()
    
    