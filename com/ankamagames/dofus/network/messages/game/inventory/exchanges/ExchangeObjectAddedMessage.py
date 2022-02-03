from com.ankamagames.dofus.network.messages.game.inventory.exchanges.ExchangeObjectMessage import ExchangeObjectMessage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from com.ankamagames.dofus.network.types.game.data.items.ObjectItem import ObjectItem
    


class ExchangeObjectAddedMessage(ExchangeObjectMessage):
    object:'ObjectItem'
    

    def init(self, object:'ObjectItem', remote:bool):
        self.object = object
        
        super().__init__(remote)
    
    