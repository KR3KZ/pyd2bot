from com.ankamagames.dofus.network.messages.game.inventory.items.InventoryContentMessage import InventoryContentMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class WatchInventoryContentMessage(InventoryContentMessage):
    

    def init(self, objects:list['ObjectItem'], kamas:int):
        
        super().__init__(objects, kamas)
    
    