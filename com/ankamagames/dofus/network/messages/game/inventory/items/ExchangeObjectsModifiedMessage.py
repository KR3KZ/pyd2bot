from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ExchangeObjectsModifiedMessage(ExchangeObjectMessage):
    object:list['ObjectItem']
    

    def init(self, object:list['ObjectItem'], remote:bool):
        self.object = object
        
        super().__init__(remote)
    
    